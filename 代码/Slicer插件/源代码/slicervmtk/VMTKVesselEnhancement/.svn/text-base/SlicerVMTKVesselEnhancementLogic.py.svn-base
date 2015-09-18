from Slicer import slicer


class SlicerVMTKVesselEnhancementLogic(object):

    def __init__(self,mainGUIClass):

        self._helper = mainGUIClass

    def ApplyFrangiVesselness(self,image,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,beta,gamma):

        self._helper.debug("Starting execution of Frangi...")

        cast = slicer.vtkImageCast()
        cast.SetInput(image)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()
        image = cast.GetOutput()

        v = slicer.vtkvmtkVesselnessMeasureImageFilter()
        v.SetInput(image)
        v.SetSigmaMin(sigmaMin)
        v.SetSigmaMax(sigmaMax)
        v.SetNumberOfSigmaSteps(numberOfSigmaSteps)
        v.SetAlpha(alpha)
        v.SetBeta(beta)
        v.SetGamma(gamma)
        v.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(v.GetOutput())
        outVolumeData.Update()
        outVolumeData.GetPointData().GetScalars().Modified()

        return outVolumeData


    def ApplySatoVesselness(self,image,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,alpha2):

	self._helper.debug(image.GetSpacing())	

        self._helper.debug("Starting execution of Sato...")

        cast = slicer.vtkImageCast()
        cast.SetInput(image)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()
        image = cast.GetOutput()

        v = slicer.vtkvmtkSatoVesselnessMeasureImageFilter()
        v.SetInput(image)
        v.SetSigmaMin(sigmaMin)
        v.SetSigmaMax(sigmaMax)
        v.SetNumberOfSigmaSteps(numberOfSigmaSteps)
        v.SetAlpha1(alpha)
        v.SetAlpha2(alpha2)
        v.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(v.GetOutput())
        outVolumeData.Update()
        outVolumeData.GetPointData().GetScalars().Modified()

        return outVolumeData


    def ApplyVED(self,image,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,beta,gamma,c,timestep,epsilon,wstrength,sensitivity,numberOfIterations,numberOfDiffusionSubIterations):

        self._helper.debug("Starting execution of VED...")

        cast = slicer.vtkImageCast()
        cast.SetInput(image)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()
        image = cast.GetOutput()

        v = slicer.vtkvmtkVesselEnhancingDiffusionImageFilter()
        v.SetInput(image)
        v.SetSigmaMin(sigmaMin)
        v.SetSigmaMax(sigmaMax)
        v.SetNumberOfSigmaSteps(numberOfSigmaSteps)
        v.SetAlpha(alpha)
        v.SetBeta(beta)
        v.SetGamma(gamma)
        v.SetC(c)
        v.SetTimeStep(timestep)
        v.SetEpsilon(epsilon)
        v.SetWStrength(wstrength)
        v.SetSensitivity(sensitivity)
        v.SetNumberOfIterations(numberOfIterations)
        v.SetNumberOfDiffusionSubIterations(numberOfDiffusionSubIterations)
        v.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(v.GetOutput())
        outVolumeData.Update()
        outVolumeData.GetPointData().GetScalars().Modified()

        return outVolumeData
        
    def ApplyVEDM(self,image,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,beta,gamma,timestep,epsilon,wstrength,sensitivity,numberOfIterations,numberOfDiffusionSubIterations):

        self._helper.debug("Starting execution of VED...")

        cast = slicer.vtkImageCast()
        cast.SetInput(image)
        cast.SetOutputScalarTypeToFloat()
        cast.Update()
        image = cast.GetOutput()

        v = slicer.vtkvmtkVesselEnhancingDiffusion3DImageFilter()
        v.SetInput(image)
        v.SetSigmaMin(sigmaMin)
        v.SetSigmaMax(sigmaMax)
        v.SetNumberOfSigmaSteps(numberOfSigmaSteps)
        v.SetAlpha(alpha)
        v.SetBeta(beta)
        v.SetGamma(gamma)
        v.SetTimeStep(timestep)
        v.SetEpsilon(epsilon)
        v.SetWStrength(wstrength)
        v.SetSensitivity(sensitivity)
        v.SetNumberOfIterations(numberOfIterations)
        v.SetNumberOfDiffusionSubIterations(numberOfDiffusionSubIterations)
        v.Update()

        outVolumeData = slicer.vtkImageData()
        outVolumeData.DeepCopy(v.GetOutput())
        outVolumeData.Update()
        outVolumeData.GetPointData().GetScalars().Modified()

        return outVolumeData



