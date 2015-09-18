from Slicer import slicer

from SlicerVMTKLevelSetContainer import SlicerVMTKLevelSetContainer

### pseudo logic class
class SlicerVMTKLevelSetLogic(object):

    def __init__(self,mainGUIClass):

        self._helper = mainGUIClass.GetHelper()

        # advanced settings, hardcoded...
        self.SigmoidRemapping = 1
        self.DerivativeSigma = 0.0
        self.FeatureDerivativeSigma = 0.0
        self.MaximumRMSError = 1E-20
        self.IsoSurfaceValue = 0.0

    def ExecuteCollidingFronts(self,inVolumeNode,lowerThreshold,higherThreshold,sourceSeedsNode,targetSeedsNode):

        self._helper.debug("Starting execution of Colliding Fronts..")

        if not inVolumeNode or not sourceSeedsNode or not targetSeedsNode:
            self._helper.debug(inVolumeNode)
            self._helper.debug(lowerThreshold)         
            self._helper.debug(higherThreshold)  
            self._helper.debug(sourceSeedsNode)  
            self._helper.debug(targetSeedsNode)         
            slicer.Application.ErrorMessage("Not enough information!!! Aborting Colliding Fronts..\n")
            return
        else:

            sourceSeedIds = slicer.vtkIdList()
            targetSeedIds = slicer.vtkIdList()

            image = inVolumeNode.GetImageData()

            cast = slicer.vtkImageCast()
            cast.SetInput(image)
            cast.SetOutputScalarTypeToFloat()
            cast.Update()
            image = cast.GetOutput()

            rasPt = sourceSeedsNode.GetNthFiducialXYZ(0)
            self._helper.debug(rasPt)
            ijkPt = self._helper.ConvertRAS2IJK(rasPt)
            self._helper.debug(ijkPt)
            sourceSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

            rasPt = targetSeedsNode.GetNthFiducialXYZ(0)
            self._helper.debug(rasPt)
            ijkPt = self._helper.ConvertRAS2IJK(rasPt)
            self._helper.debug(ijkPt)
            targetSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

            scalarRange = image.GetScalarRange()
            self._helper.debug("CF: after converting seeds")

            threshold = slicer.vtkImageThreshold()
            threshold.SetInput(image)
            threshold.ThresholdBetween(lowerThreshold, higherThreshold)
            threshold.ReplaceInOff()
            threshold.ReplaceOutOn()
            threshold.SetOutValue(scalarRange[0] - scalarRange[1])
            threshold.Update()

            self._helper.debug("CF: after thresholding")
    
            scalarRange = threshold.GetOutput().GetScalarRange()

            thresholdedImage = threshold.GetOutput()

            shiftScale = slicer.vtkImageShiftScale()
            shiftScale.SetInput(thresholdedImage)
            shiftScale.SetShift(-scalarRange[0])
            shiftScale.SetScale(1/(scalarRange[1]-scalarRange[0]))
            shiftScale.Update()
            
            speedImage = shiftScale.GetOutput()

            self._helper.debug("CF: after shiftScale")            

            collidingFronts = slicer.vtkvmtkCollidingFrontsImageFilter()
            collidingFronts.SetInput(speedImage)
            collidingFronts.SetSeeds1(sourceSeedIds)
            collidingFronts.SetSeeds2(targetSeedIds)
            collidingFronts.ApplyConnectivityOn()
            collidingFronts.StopOnTargetsOn()
            collidingFronts.Update()

            self._helper.debug("CF: after CF")

            subtract = slicer.vtkImageMathematics()
            subtract.SetInput(collidingFronts.GetOutput())
            subtract.SetOperationToAddConstant()
            subtract.SetConstantC(-10.0 * collidingFronts.GetNegativeEpsilon())
            subtract.Update()

            self._helper.debug("CF: after substract")

            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(subtract.GetOutput())
            outVolumeData.Update()

            # volume calculated...

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,collidingFronts.GetNegativeEpsilon())

            self._helper.debug("Colliding Fronts done...")

            return outputContainer

            # run completed

    def ExecuteFastMarching(self,inVolumeNode,lowerThreshold,higherThreshold,sourceSeedsNode,targetSeedsNode):

        self._helper.debug("Starting execution of Fast Marching...")

        if not inVolumeNode or not sourceSeedsNode:
            self._helper.debug(inVolumeNode)
            self._helper.debug(lowerThreshold)         
            self._helper.debug(higherThreshold)  
            self._helper.debug(sourceSeedsNode)  
            self._helper.debug(targetSeedsNode)         
            slicer.Application.ErrorMessage("Not enough information!!! Aborting Fast Marching..\n")
            return
        else:

            sourceSeedIds = slicer.vtkIdList()
            targetSeedIds = slicer.vtkIdList()

            image = inVolumeNode.GetImageData()

            cast = slicer.vtkImageCast()
            cast.SetInput(image)
            cast.SetOutputScalarTypeToFloat()
            cast.Update()
            image = cast.GetOutput()

            for i in range(sourceSeedsNode.GetNumberOfFiducials()):
                rasPt = sourceSeedsNode.GetNthFiducialXYZ(i)
                ijkPt = self._helper.ConvertRAS2IJK(rasPt)
                sourceSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

            if targetSeedsNode:
                for i in range(targetSeedsNode.GetNumberOfFiducials()):
                    rasPt = targetSeedsNode.GetNthFiducialXYZ(i)
                    ijkPt = self._helper.ConvertRAS2IJK(rasPt)
                    targetSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

            scalarRange = image.GetScalarRange()

            threshold = slicer.vtkImageThreshold()
            threshold.SetInput(image)
            threshold.ThresholdBetween(lowerThreshold,higherThreshold)
            threshold.ReplaceInOff()
            threshold.ReplaceOutOn()
            threshold.SetOutValue(scalarRange[0] - scalarRange[1])
            threshold.Update()

            scalarRange = threshold.GetOutput().GetScalarRange()

            thresholdedImage = threshold.GetOutput()

            shiftScale = slicer.vtkImageShiftScale()
            shiftScale.SetInput(thresholdedImage)
            shiftScale.SetShift(-scalarRange[0])
            shiftScale.SetScale(1/(scalarRange[1]-scalarRange[0]))
            shiftScale.Update()

            speedImage = shiftScale.GetOutput()

            fastMarching = slicer.vtkvmtkFastMarchingUpwindGradientImageFilter()
            fastMarching.SetInput(speedImage)
            fastMarching.SetSeeds(sourceSeedIds)
            fastMarching.GenerateGradientImageOff()
            fastMarching.SetTargetOffset(100.0)
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
                subtract = slicer.vtkImageThreshold()
                subtract.SetInput(fastMarching.GetOutput())
                subtract.ThresholdByLower(1000)#better value soon
                subtract.ReplaceInOff()
                subtract.ReplaceOutOn()
                subtract.SetOutValue(-1)
                subtract.Update()

            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(subtract.GetOutput())
            outVolumeData.Update()

            # volume calculated...

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,0.0)

            self._helper.debug("Fast Marching done...")

            return outputContainer

            # run completed



    def ExecuteThreshold(self,inVolumeNode,lowerThreshold,higherThreshold):


        self._helper.debug("Starting execution of Threshold...")


        if not inVolumeNode:
            slicer.Application.ErrorMessage("No input volume found. Aborting Threshold..\n")
            return
        else:

            image = inVolumeNode.GetImageData()

            cast = slicer.vtkImageCast()
            cast.SetInput(image)
            cast.SetOutputScalarTypeToFloat()
            cast.Update()
            image = cast.GetOutput()

            scalarRange = image.GetScalarRange()


            threshold = slicer.vtkImageThreshold()
            threshold.SetInput(image)

            threshold.ThresholdBetween(lowerThreshold,higherThreshold)

            threshold.ReplaceInOff()
            threshold.ReplaceOutOn()
            threshold.SetInValue(-1.0)
            threshold.SetOutValue(1.0)
            threshold.Update()

            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(threshold.GetOutput())
            outVolumeData.Update()

            # volume calculated...

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,0.0)

            self._helper.debug("Threshold done...")
    
            return outputContainer

            # run completed

    def ExecuteIsosurface(self,inVolumeNode,value):


        self._helper.debug("Starting execution of Isosurface...")

        if not inVolumeNode:
            slicer.Application.ErrorMessage("No input volume found. Aborting Isosurface..\n")
            return
        else:

            image = inVolumeNode.GetImageData()

            cast = slicer.vtkImageCast()
            cast.SetInput(image)
            cast.SetOutputScalarTypeToFloat()
            cast.Update()
            image = cast.GetOutput()

            imageMathematics = slicer.vtkImageMathematics()
            imageMathematics.SetInput(image)
            imageMathematics.SetConstantK(-1.0)
            imageMathematics.SetOperationToMultiplyByK()
            imageMathematics.Update()

            subtract = slicer.vtkImageMathematics()
            subtract.SetInput(imageMathematics.GetOutput())
            subtract.SetOperationToAddConstant()
            subtract.SetConstantC(value)
            subtract.Update()

            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(subtract.GetOutput())

            outVolumeData.Update()

            # volume calculated...

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,10)

            self._helper.debug("Isosurface done...")

            return outputContainer

            # run completed


    def ExecuteSeeds(self,inVolumeNode,sourceSeedsNode):


        self._helper.debug("Starting execution of seeds...")

        if not inVolumeNode or not sourceSeedsNode:
            slicer.Application.ErrorMessage("Not enough information. Aborting Seeds..\n")
            return
        else:

            image = inVolumeNode.GetImageData()

            cast = slicer.vtkImageCast()
            cast.SetInput(image)
            cast.SetOutputScalarTypeToFloat()
            cast.Update()
            image = cast.GetOutput()

            seeds = sourceSeedsNode
    
            initialLevelSets = slicer.vtkImageData()
            initialLevelSets.DeepCopy(image)
            initialLevelSets.Update()

            levelSetsInputScalars = initialLevelSets.GetPointData().GetScalars()
            levelSetsInputScalars.FillComponent(0,1.0)

            for i in range(seeds.GetNumberOfFiducials()):
                rasPt = seeds.GetNthFiducialXYZ(i)
                ijkPt = self._helper.ConvertRAS2IJK(rasPt)
                id = image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2]))
                levelSetsInputScalars.SetComponent(id,0,-1.0)

            dilateErode = slicer.vtkImageDilateErode3D()
            dilateErode.SetInput(initialLevelSets)
            dilateErode.SetDilateValue(-1.0)
            dilateErode.SetErodeValue(1.0)
            dilateErode.SetKernelSize(3,3,3)
            dilateErode.Update()

            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(dilateErode.GetOutput())
            outVolumeData.Update()

            # volume calculated...

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,0.0)

            self._helper.debug("Seeds done...")

            return outputContainer

            # run completed




    def BuildGradientBasedFeatureImage(self,imageData):

        cast = slicer.vtkImageCast()
        cast.SetInput(imageData)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()

        if (self.DerivativeSigma > 0.0):
            gradientMagnitude = slicer.vtkvmtkGradientMagnitudeRecursiveGaussianImageFilter()
            gradientMagnitude.SetInput(cast.GetOutput())
            gradientMagnitude.SetSigma(self.DerivativeSigma)
            gradientMagnitude.SetNormalizeAcrossScale(0)
            gradientMagnitude.Update()
        else:
            gradientMagnitude = slicer.vtkvmtkGradientMagnitudeImageFilter()
            gradientMagnitude.SetInput(cast.GetOutput())
            gradientMagnitude.Update()

        featureImage = None
        if self.SigmoidRemapping==1:
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


    def ExecuteGeodesic(self,origInVolumeNode,inVolumeNode,numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,calculateFeatureImage):

        self._helper.debug("Starting execution of Geodesic..")

        if not inVolumeNode or not origInVolumeNode:
            slicer.Application.ErrorMessage("Not enough information!!! Aborting Geodesic..\n")
            return
        else:

            cast = slicer.vtkImageCast()
            cast.SetInput(origInVolumeNode.GetImageData())
            cast.SetOutputScalarTypeToFloat()
            cast.Update()

            origImage = cast.GetOutput()
            image = inVolumeNode.GetImageData()

            levelSets = slicer.vtkvmtkGeodesicActiveContourLevelSetImageFilter()
            if calculateFeatureImage==1:
                levelSets.SetFeatureImage(self.BuildGradientBasedFeatureImage(origImage))
            else:
                levelSets.SetFeatureImage(origImage)
            levelSets.SetDerivativeSigma(self.FeatureDerivativeSigma)
            levelSets.SetAutoGenerateSpeedAdvection(1)
            levelSets.SetPropagationScaling(propagationScaling)
            levelSets.SetCurvatureScaling(curvatureScaling)
            levelSets.SetAdvectionScaling(advectionScaling)


            levelSets.SetInput(image)
            levelSets.SetNumberOfIterations(numberOfIterations)
            levelSets.SetIsoSurfaceValue(self.IsoSurfaceValue)
            levelSets.SetMaximumRMSError(self.MaximumRMSError)
            levelSets.SetInterpolateSurfaceLocation(1)
            levelSets.SetUseImageSpacing(1)
            levelSets.Update()


            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(levelSets.GetOutput())
            outVolumeData.Update()

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,0.0)

            return outputContainer


    def ExecuteCurves(self,origInVolumeNode,inVolumeNode,numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,calculateFeatureImage):

        self._helper.debug("Starting execution of Curves..")

        if not inVolumeNode or not origInVolumeNode:
            slicer.Application.ErrorMessage("Not enough information!!! Aborting Geodesic..\n")
            return
        else:

            cast = slicer.vtkImageCast()
            cast.SetInput(origInVolumeNode.GetImageData())
            cast.SetOutputScalarTypeToFloat()
            cast.Update()

            origImage = cast.GetOutput()
            image = inVolumeNode.GetImageData()

            levelSets = slicer.vtkvmtkCurvesLevelSetImageFilter()
            self._helper.debug("FeatureImageCalc: " + str(calculateFeatureImage))
            if calculateFeatureImage==1:
                levelSets.SetFeatureImage(self.BuildGradientBasedFeatureImage(origImage))
            else:
                levelSets.SetFeatureImage(origImage)
            levelSets.SetDerivativeSigma(self.FeatureDerivativeSigma)
            levelSets.SetAutoGenerateSpeedAdvection(1)
            levelSets.SetPropagationScaling(propagationScaling)
            levelSets.SetCurvatureScaling(curvatureScaling)
            levelSets.SetAdvectionScaling(advectionScaling)


            levelSets.SetInput(image)
            levelSets.SetNumberOfIterations(numberOfIterations)
            levelSets.SetIsoSurfaceValue(self.IsoSurfaceValue)
            levelSets.SetMaximumRMSError(self.MaximumRMSError)
            levelSets.SetInterpolateSurfaceLocation(1)
            levelSets.SetUseImageSpacing(1)
            levelSets.Update()


            matrix = slicer.vtkMatrix4x4()
            inVolumeNode.GetIJKToRASMatrix(matrix)

            outVolumeData = slicer.vtkImageData()
            outVolumeData.DeepCopy(levelSets.GetOutput())
            outVolumeData.Update()

            outVolumeNode = slicer.vtkMRMLScalarVolumeNode()
            outVolumeNode.SetAndObserveImageData(outVolumeData)
            outVolumeNode.SetIJKToRASMatrix(matrix)

            outputContainer = SlicerVMTKLevelSetContainer(outVolumeNode,0.0)

            return outputContainer


    ###
    ### marching cubes algorithm, takes imageData and returns polyData
    ###
    def MarchingCubes(self,image,matrix,threshold):

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

        return result



