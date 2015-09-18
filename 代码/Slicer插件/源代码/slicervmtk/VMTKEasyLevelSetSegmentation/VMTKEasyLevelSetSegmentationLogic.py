from Slicer import slicer

class VMTKEasyLevelSetSegmentationLogic(object):

    def __init__(self,parentClass):

        self._parentClass = parentClass

        # advanced settings, hardcoded...
        self._sigmoidRemapping = 1
        self._derivativeSigma = 0.0
        self._featureDerivativeSigma = 0.0
        self._maximumRMSError = 1E-20
        self._isoSurfaceValue = 0.0

        #volume rendering settings
        self._mapper = None
        self._piecewiseFunction = None
        self._transferFunction = None
        self._volumeProperty = None
        self._volume = None

    def ExecuteFM(self,image,lowerThreshold,higherThreshold,sourceSeedIds,targetSeedIds,sideBranches):

        self._parentClass.GetHelper().debug("Starting FM..")

        cast = slicer.vtkImageCast()
        cast.SetInput(image)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()
        image = cast.GetOutput()

        scalarRange = image.GetScalarRange()

        imageDimensions = image.GetDimensions()
        maxImageDimensions = max(imageDimensions)

        threshold = slicer.vtkImageThreshold()
        threshold.SetInput(image)
        threshold.ThresholdBetween(lowerThreshold,higherThreshold)
        threshold.ReplaceInOff()
        threshold.ReplaceOutOn()
        threshold.SetOutValue(scalarRange[0] - scalarRange[1])
        threshold.Update()

        thresholdedImage = threshold.GetOutput()

        scalarRange = thresholdedImage.GetScalarRange()

        shiftScale = slicer.vtkImageShiftScale()
        shiftScale.SetInput(thresholdedImage)
        shiftScale.SetShift(-scalarRange[0])
        shiftScale.SetScale(1/(scalarRange[1]-scalarRange[0]))
        shiftScale.Update()

        speedImage = shiftScale.GetOutput()

        if sideBranches:
            # ignore sidebranches, use colliding fronts
            self._parentClass.GetHelper().debug("COLLIDINGFRONTS")
            fastMarching = slicer.vtkvmtkCollidingFrontsImageFilter()
            fastMarching.SetInput(speedImage)
            fastMarching.SetSeeds1(sourceSeedIds)
            fastMarching.SetSeeds2(targetSeedIds)
            fastMarching.ApplyConnectivityOn()
            fastMarching.StopOnTargetsOn()            
            fastMarching.Update()

            subtract = slicer.vtkImageMathematics()
            subtract.SetInput(fastMarching.GetOutput())
            subtract.SetOperationToAddConstant()
            subtract.SetConstantC(-10*fastMarching.GetNegativeEpsilon())
            subtract.Update()

        else:
            fastMarching = slicer.vtkvmtkFastMarchingUpwindGradientImageFilter()
            fastMarching.SetInput(speedImage)
            fastMarching.SetSeeds(sourceSeedIds)
            fastMarching.GenerateGradientImageOn()
            fastMarching.SetTargetOffset(0.0)
            fastMarching.SetTargets(targetSeedIds)
            if targetSeedIds.GetNumberOfIds() > 0:
                fastMarching.SetTargetReachedModeToOneTarget()
            else:
                fastMarching.SetTargetReachedModeToNoTargets()
            fastMarching.Update()

            if targetSeedIds.GetNumberOfIds() > 0:
                subtract = slicer.vtkImageMathematics()
                subtract.SetInput(fastMarching.GetOutput())
                subtract.SetOperationToAddConstant()
                subtract.SetConstantC(-fastMarching.GetTargetValue())
                subtract.Update()

            else:
                #self._parentClass.GetHelper().debug("No target mode "+str(fastMarching.GetTargetValue()))
                subtract = slicer.vtkImageThreshold()
                subtract.SetInput(fastMarching.GetOutput())
                subtract.ThresholdByLower(2000) # TODO find robuste value
                subtract.ReplaceInOff()
                subtract.ReplaceOutOn()
                subtract.SetOutValue(-1)
                subtract.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(subtract.GetOutput())
        outVolumeData.Update()
        
        self._parentClass.GetHelper().debug("End of FM..")

        return outVolumeData

    def BuildSimpleLabelMap(self,image,inValue,outValue):

        threshold = slicer.vtkImageThreshold()
        threshold.SetInput(image)
        threshold.ThresholdByLower(0)
        threshold.ReplaceInOn()
        threshold.ReplaceOutOn()
        threshold.SetOutValue(outValue)
        threshold.SetInValue(inValue)
        threshold.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(threshold.GetOutput())
        outVolumeData.Update()

        return outVolumeData


    def BuildGradientBasedFeatureImage(self,imageData):

        cast = slicer.vtkImageCast()
        cast.SetInput(imageData)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()

        if (self._derivativeSigma > 0.0):
            gradientMagnitude = slicer.vtkvmtkGradientMagnitudeRecursiveGaussianImageFilter()
            gradientMagnitude.SetInput(cast.GetOutput())
            gradientMagnitude.SetSigma(self._derivativeSigma)
            gradientMagnitude.SetNormalizeAcrossScale(0)
            gradientMagnitude.Update()
        else:
            gradientMagnitude = slicer.vtkvmtkGradientMagnitudeImageFilter()
            gradientMagnitude.SetInput(cast.GetOutput())
            gradientMagnitude.Update()

        featureImage = None
        if self._sigmoidRemapping==1:
            scalarRange = gradientMagnitude.GetOutput().GetPointData().GetScalars().GetRange()
            inputMinimum = scalarRange[0]
            inputMaximum = scalarRange[1]
            alpha = - (inputMaximum - inputMinimum) / 6.0
            beta = (inputMaximum + inputMinimum) / 2.0
            sigmoid = slicer.vtkvmtkSigmoidImageFilter()
            sigmoid.SetInput(gradientMagnitude.GetOutput())
            sigmoid.SetAlpha(alpha)
            sigmoid.SetBeta(beta)
            sigmoid.SetOutputMinimum(0.0)
            sigmoid.SetOutputMaximum(1.0)
            sigmoid.Update()
            featureImage = sigmoid.GetOutput()
        else:
            boundedReciprocal = slicer.vtkvmtkBoundedReciprocalImageFilter()
            boundedReciprocal.SetInput(gradientMagnitude.GetOutput())
            boundedReciprocal.Update()
            featureImage = boundedReciprocal.GetOutput()

        featureImageOutput = slicer.vtkImageData()
        featureImageOutput.DeepCopy(featureImage)
        featureImageOutput.Update()

        return featureImageOutput


    def ExecuteGAC(self,origImage,segmentationImage,numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,method):

        self._parentClass.GetHelper().debug("Starting GAC..")

        calculateFeatureImage = 1

        cast = slicer.vtkImageCast()
        cast.SetInput(origImage)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()

        if method=='curves':
            levelSets = slicer.vtkvmtkCurvesLevelSetImageFilter()
        else:
            levelSets = slicer.vtkvmtkGeodesicActiveContourLevelSetImageFilter()

        if calculateFeatureImage==1:
            levelSets.SetFeatureImage(self.BuildGradientBasedFeatureImage(origImage))
        else:
            levelSets.SetFeatureImage(origImage)
        levelSets.SetDerivativeSigma(self._featureDerivativeSigma)
        levelSets.SetAutoGenerateSpeedAdvection(1)
        levelSets.SetPropagationScaling(propagationScaling)
        levelSets.SetCurvatureScaling(curvatureScaling)
        levelSets.SetAdvectionScaling(advectionScaling)
        levelSets.SetInput(segmentationImage)
        levelSets.SetNumberOfIterations(numberOfIterations)
        levelSets.SetIsoSurfaceValue(self._isoSurfaceValue)
        levelSets.SetMaximumRMSError(self._maximumRMSError)
        levelSets.SetInterpolateSurfaceLocation(1)
        levelSets.SetUseImageSpacing(1)
        levelSets.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(levelSets.GetOutput())
        outVolumeData.Update()

        self._parentClass.GetHelper().debug("End of GAC..")

        return outVolumeData

    # volume rendering
    def VolumeRendering(self,image,ijkToRasMatrix,minV,maxV,color):

        self._mapper = slicer.vtkFixedPointVolumeRayCastMapper()
        self._piecewiseFunction = slicer.vtkPiecewiseFunction()
        self._transferFunction = slicer.vtkColorTransferFunction()
        self._volumeProperty = slicer.vtkVolumeProperty()
        self._volume = slicer.vtkVolume()

        scalarRange = image.GetPointData().GetScalars().GetRange()
        self._parentClass.GetHelper().debug(scalarRange)

        self._volumeProperty.SetShade(1)
        self._volumeProperty.SetAmbient(0.3)
        self._volumeProperty.SetDiffuse(0.6)
        self._volumeProperty.SetSpecular(0.5)
        self._volumeProperty.SetSpecularPower(40.0)
        self._volumeProperty.SetScalarOpacity(self._piecewiseFunction)
        self._volumeProperty.SetColor(self._transferFunction)
        self._volumeProperty.SetInterpolationTypeToLinear()
        self._volumeProperty.ShadeOn()

        self._volume.SetProperty(self._volumeProperty)
        self._volume.SetMapper(self._mapper)

        self._mapper.SetInput(image)
        self._volume.PokeMatrix(ijkToRasMatrix)

        self._piecewiseFunction.RemoveAllPoints()
        # bandpass
        self._piecewiseFunction.AddPoint(scalarRange[0], 0.0)
        self._piecewiseFunction.AddPoint(minV-1, 0.0)
        self._piecewiseFunction.AddPoint(minV, 1.0, 0.5, 1.0)
        self._piecewiseFunction.AddPoint(maxV, 1.0, 0.5, 1.0)
        if (maxV < scalarRange[1]):
            self._piecewiseFunction.AddPoint(maxV + 0.1, 0.0)
            if (maxV+0.1 < scalarRange[1]):
                self._piecewiseFunction.AddPoint(maxV + 0.1, 0.0)
                self._piecewiseFunction.AddPoint(scalarRange[1], 0.0)

        self._piecewiseFunction.ClampingOff()

        self._transferFunction.RemoveAllPoints()
        self._transferFunction.AddRGBPoint(minV, color[0], color[1], color[2])
        self._transferFunction.AddRGBPoint(maxV, color[0], color[1], color[2])

    ###
    ### marching cubes algorithm, takes imageData and returns polyData
    ###
    def MarchingCubes(self,image,matrix,threshold):

        self._parentClass.GetHelper().debug("Starting MarchingCubes..")

        transformIJKtoRAS = slicer.vtkTransform()
        transformIJKtoRAS.SetMatrix(matrix)

        marchingCubes = slicer.vtkMarchingCubes()
        marchingCubes.SetInput(image)
        marchingCubes.SetValue(0,threshold)
        marchingCubes.ComputeScalarsOn()
        marchingCubes.ComputeGradientsOn()
        marchingCubes.ComputeNormalsOn()
        marchingCubes.GetOutput().ReleaseDataFlagOn()
        marchingCubes.Update()

        if transformIJKtoRAS.GetMatrix().Determinant() < 0:
            self.debug("Determinant smaller than 0")
            reverser = slicer.vtkReverseSense()
            reverser.SetInput(marchingCubes.GetOutput())
            reverser.ReverseNormalsOn()
            reverser.GetOutput().ReleaseDataFlagOn()
            reverser.Update()
            correctedOutput = reverser.GetOutput()
        else:
            correctedOutput = marchingCubes.GetOutput()

        transformer = slicer.vtkTransformPolyDataFilter()
        transformer.SetInput(correctedOutput)
        transformer.SetTransform(transformIJKtoRAS)
        transformer.GetOutput().ReleaseDataFlagOn()
        transformer.Update()

        normals = slicer.vtkPolyDataNormals()
        normals.ComputePointNormalsOn()
        normals.SetInput(transformer.GetOutput())
        normals.SetFeatureAngle(60)
        normals.SetSplitting(1)
        normals.GetOutput().ReleaseDataFlagOn()
        normals.Update()
        
        stripper = slicer.vtkStripper()
        stripper.SetInput(normals.GetOutput())
        stripper.GetOutput().ReleaseDataFlagOff()
        stripper.Update()
        stripper.GetOutput().Update()

        result = slicer.vtkPolyData()
        result.DeepCopy(stripper.GetOutput())
        result.Update()

        self._parentClass.GetHelper().debug("End MarchingCubes..")

        return result

