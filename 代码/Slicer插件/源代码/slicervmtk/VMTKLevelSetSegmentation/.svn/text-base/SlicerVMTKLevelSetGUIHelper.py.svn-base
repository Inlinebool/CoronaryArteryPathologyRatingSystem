from Slicer import slicer
from time import strftime
from math import floor

from SlicerVMTKLevelSetContainer import SlicerVMTKLevelSetContainer

###
### Helper class for VMTK Level Set..
###
class SlicerVMTKLevelSetGUIHelper(object):


    def __init__(self,mainGUIClass):

        self._mainGUIClass = mainGUIClass
        self._isInteractiveModeActive = 0
        self._interactiveModeHandlerClass = None

        self._renderWindowInteractor = None
        self._redSliceInteractor = None
        self._yellowSliceInteractor = None
        self._greenSliceInteractor = None

    def SetIsInteractiveMode(self,onoff,handlerClass):
        self._isInteractiveModeActive = onoff
        self._interactiveModeHandlerClass = handlerClass

    def GetIsInteractiveMode(self):
        return self._isInteractiveModeActive


    def debug(self,msg):

        '''debug prints to stdout (better than print because of flush)'''

        # declaration of new variable without type specification
        debugMode = 0

        if debugMode: # debugMode is a bool

            # the print statement needs strings as input, so every value to output has to be
            # casted
            print "[slicerVMTKLevelSet " + strftime("%H:%M:%S") + "] " + str(msg)
            import sys
            sys.stdout.flush()

    ###
    ### registers the interactors passed through from the parent class
    ###
    def RegisterInteractors(self, renderWindowInteractor, redSliceInteractor, yellowSliceInteractor, greenSliceInteractor):

        self._renderWindowInteractor = renderWindowInteractor
        self._redSliceInteractor = redSliceInteractor
        self._yellowSliceInteractor = yellowSliceInteractor
        self._greenSliceInteractor = greenSliceInteractor

    ###
    ### click handlers for the 3D render window
    ###
    def HandleClickInRenderWindow(self):

        if self._isInteractiveModeActive:

            self.debug("Clicked in 3D")

            interactor = self._renderWindowInteractor

            coordinates = interactor.GetLastEventPosition()
            size = interactor.GetRenderWindow().GetSize()
            self.debug("X" + str(coordinates[0]))
            self.debug("Y" + str(coordinates[1]))

            coordinates[1] = size[1] - coordinates[1] - 1

            viewerWidget = slicer.ApplicationGUI.GetViewerWidget()

            pick = viewerWidget.Pick(coordinates[0], coordinates[1])

            if pick:

                coordinatesRAS = viewerWidget.GetPickedRAS()

                coordinatesRAS = coordinatesRAS

                self.debug(coordinatesRAS)
                self._interactiveModeHandlerClass.HandleClickInSliceWindowWithCoordinates(coordinatesRAS)
            else:
                self.debug("no pickable coordinates")

    ###
    ### click handlers for the slices
    ###
    def HandleClickInRedSliceWindow(self):
        self.HandleClickInSliceWindow("Red",self._redSliceInteractor)

    def HandleClickInYellowSliceWindow(self):
        self.HandleClickInSliceWindow("Yellow",self._yellowSliceInteractor)

    def HandleClickInGreenSliceWindow(self):
        self.HandleClickInSliceWindow("Green",self._greenSliceInteractor)

    def HandleClickInSliceWindow(self,which,interactor):

        if self._isInteractiveModeActive:
            
            self.debug("Clicked on " +which + "Slice")

            coordinates = interactor.GetLastEventPosition()

            self.debug(coordinates[0])
            self.debug(coordinates[1])

            coordinatesRAS = self.ConvertCoordinates2RAS(which,coordinates)

            self._interactiveModeHandlerClass.HandleClickInSliceWindowWithCoordinates(coordinatesRAS)
 


    ###
    ### convert coordinates to RAS
    ###
    def ConvertCoordinates2RAS(self,which,coordinates):
        # convert to RAS
        inPt = [coordinates[0], coordinates[1], 0, 1]
        matrixRAS = slicer.ApplicationGUI.GetMainSliceGUI(which).GetLogic().GetSliceNode().GetXYToRAS()
        rasPt = matrixRAS.MultiplyPoint(*inPt)
        return rasPt

    ###
    ### convert coordinates to IJK
    ###
    def ConvertCoordinates2IJK(self,which,coordinates):
        #need RAS
        rasPt = self.ConvertCoordinates2RAS(which,coordinates)

        #convert to IJK
        node = self._mainGUIClass.GetScriptedModuleNode()
        if node:
            inVolume = node.GetParameter('InputVolumeRef')
            if not inVolume:
                slicer.Application.ErrorMessage("No input volume found\n")
                return
            else:
                matrixIJK = slicer.vtkMatrix4x4()
                inVolume.GetRASToIJKMatrix(matrixIJK)
                ijkPt = matrixIJK.MultiplyPoint(*rasPt)
                return ijkPt
            
    ###
    ### convert RAS to IJK
    ###
    def ConvertRAS2IJK(self,coordinates):

        rasPt = coordinates
        rasPt.append(1)

        #convert to IJK
        node = self._mainGUIClass.GetScriptedModuleNode()
        if node:
            inVolume = node.GetParameter('InputVolumeRef')
            if not inVolume:
                slicer.Application.ErrorMessage("No input volume found\n")
                return
            else:
                matrixIJK = slicer.vtkMatrix4x4()
                inVolume.GetRASToIJKMatrix(matrixIJK)
                #self.debug(matrixIJK)
                ijkPt = matrixIJK.MultiplyPoint(*rasPt)
                return ijkPt

    def SetAndMergeInitVolume(self,resultContainer):

        scene = self._mainGUIClass.GetLogic().GetMRMLScene()

        volumeNode = resultContainer.GetNode()
        threshold = resultContainer.GetThreshold()

        if self._mainGUIClass._outInitVolume == None:

            # no node so far

            self._mainGUIClass._outInitVolume = slicer.vtkMRMLScalarVolumeNode()
            self._mainGUIClass._outInitVolume.SetName("VMTK Level-Set Initialization Output Volume")
            self._mainGUIClass._outInitVolume.SetScene(scene)
            self._mainGUIClass._outInitVolume.SetAndObserveImageData(slicer.vtkImageData())
            scene.AddNode(self._mainGUIClass._outInitVolume)

            self._mainGUIClass._outInitVolumeLast = slicer.vtkMRMLScalarVolumeNode()
            self._mainGUIClass._outInitVolumeLast.SetName("VMTK Level-Set Initialization Output Volume (Last Step)")
            self._mainGUIClass._outInitVolumeLast.SetScene(scene)
            scene.AddNode(self._mainGUIClass._outInitVolumeLast)

        matrix = slicer.vtkMatrix4x4()

        # copy current outInitVolume to outInitVolumeLast
        self._mainGUIClass._outInitVolumeLast.SetAndObserveImageData(self._mainGUIClass._outInitVolume.GetImageData())
        self._mainGUIClass._outInitVolume.GetIJKToRASMatrix(matrix)
        self._mainGUIClass._outInitVolumeLast.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outInitVolumeLast.SetModifiedSinceRead(1)

        volumeNodeData = volumeNode.GetImageData()

        # merge the oldVolume with volumeNode if oldVolume has already content
        if self._mainGUIClass._outInitVolume.GetImageData().GetPointData().GetScalars():
            # oldVolume has already content
            minFilter = slicer.vtkImageMathematics()
            minFilter.SetOperationToMin()
            minFilter.SetInput1(self._mainGUIClass._outInitVolume.GetImageData()) #the old one
            minFilter.SetInput2(volumeNode.GetImageData()) #the new one
            minFilter.Update()
            volumeNodeData.DeepCopy(minFilter.GetOutput())

        # copy new volume to outInitVolume
        volumeNode.GetIJKToRASMatrix(matrix)
        self._mainGUIClass._outInitVolume.SetAndObserveImageData(volumeNodeData)
        self._mainGUIClass._outInitVolume.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outInitVolume.SetModifiedSinceRead(1)

        outputContainer = SlicerVMTKLevelSetContainer(self._mainGUIClass._outInitVolume,threshold)

        return outputContainer

    def UndoInit(self):

        # copy outInitVolumeLast to outInitVolume

        matrix = slicer.vtkMatrix4x4()
        self._mainGUIClass._outInitVolumeLast.GetIJKToRASMatrix(matrix)

        self._mainGUIClass._outInitVolume.SetAndObserveImageData(self._mainGUIClass._outInitVolumeLast.GetImageData())
        self._mainGUIClass._outInitVolume.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outInitVolume.SetModifiedSinceRead(1)


        outputContainer = SlicerVMTKLevelSetContainer(self._mainGUIClass._outInitVolume,0.0)

        return outputContainer


    def SetAndMergeEvolVolume(self,resultContainer):

        scene = self._mainGUIClass.GetLogic().GetMRMLScene()

        volumeNode = resultContainer.GetNode()
        threshold = resultContainer.GetThreshold()

        if self._mainGUIClass._outEvolVolume == None:

            # no node so far

            self._mainGUIClass._outEvolVolume = slicer.vtkMRMLScalarVolumeNode()
            self._mainGUIClass._outEvolVolume.SetName("VMTK Level-Set Evolution Output Volume")
            self._mainGUIClass._outEvolVolume.SetScene(scene)
            self._mainGUIClass._outEvolVolume.SetAndObserveImageData(slicer.vtkImageData())
            scene.AddNode(self._mainGUIClass._outEvolVolume)

            self._mainGUIClass._outEvolVolumeLast = slicer.vtkMRMLScalarVolumeNode()
            self._mainGUIClass._outEvolVolumeLast.SetName("VMTK Level-Set Evolution Output Volume (Last Step)")
            self._mainGUIClass._outEvolVolumeLast.SetScene(scene)
            self._mainGUIClass._outEvolVolumeLast.SetAndObserveImageData(slicer.vtkImageData())
            scene.AddNode(self._mainGUIClass._outEvolVolumeLast)

        matrix = slicer.vtkMatrix4x4()

        # copy current outEvolVolume to outEvolVolumeLast
        self._mainGUIClass._outEvolVolumeLast.SetAndObserveImageData(self._mainGUIClass._outEvolVolume.GetImageData())
        self._mainGUIClass._outEvolVolume.GetIJKToRASMatrix(matrix)
        self._mainGUIClass._outEvolVolumeLast.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outEvolVolumeLast.SetModifiedSinceRead(1)

        volumeNodeData = volumeNode.GetImageData()

        # merge the oldVolume with volumeNode if oldVolume has already content
        if self._mainGUIClass._outEvolVolume.GetImageData().GetPointData().GetScalars():
            # evolVolumeLast has already content
            minFilter = slicer.vtkImageMathematics()
            minFilter.SetOperationToMin()
            minFilter.SetInput1(self._mainGUIClass._outEvolVolume.GetImageData()) #the old one
            minFilter.SetInput2(volumeNode.GetImageData()) #the new one
            minFilter.Update()
            volumeNodeData.DeepCopy(minFilter.GetOutput())

        # copy new volume to outEvolVolume
        volumeNode.GetIJKToRASMatrix(matrix)
        self._mainGUIClass._outEvolVolume.SetAndObserveImageData(volumeNodeData)
        self._mainGUIClass._outEvolVolume.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outEvolVolume.SetModifiedSinceRead(1)

        outputContainer = SlicerVMTKLevelSetContainer(self._mainGUIClass._outEvolVolume,threshold)

        return outputContainer


    def UndoEvol(self):

        # copy outEvolVolumeLast to outEvolVolume

        matrix = slicer.vtkMatrix4x4()
        self._mainGUIClass._outEvolVolumeLast.GetIJKToRASMatrix(matrix)

        self._mainGUIClass._outEvolVolume.SetAndObserveImageData(self._mainGUIClass._outEvolVolumeLast.GetImageData())
        self._mainGUIClass._outEvolVolume.SetIJKToRASMatrix(matrix)
        self._mainGUIClass._outEvolVolume.SetModifiedSinceRead(1)


        outputContainer = SlicerVMTKLevelSetContainer(self._mainGUIClass._outEvolVolume,0.0)

        return outputContainer



    def GenerateInitializationModel(self,resultContainer):

        matrix = slicer.vtkMatrix4x4()

        image = resultContainer.GetNode().GetImageData()

        resultContainer.GetNode().GetIJKToRASMatrix(matrix)
        threshold = resultContainer.GetThreshold()

        polyData = slicer.vtkPolyData()

        if image.GetPointData().GetScalars():
            # marching Cubes, only if image has content
            polyData.DeepCopy(self._mainGUIClass.GetMyLogic().MarchingCubes(image,matrix,threshold))

        scene = self._mainGUIClass.GetLogic().GetMRMLScene()

        if self._mainGUIClass._outInitModel == None:
            # no node so far
            self._mainGUIClass._outInitModel = slicer.vtkMRMLModelNode()
            self._mainGUIClass._outInitModel.SetName("VMTK Level-Set Initialization Output Model")
            self._mainGUIClass._outInitModel.SetAndObservePolyData(slicer.vtkPolyData())
            self._mainGUIClass._outInitModel.SetScene(scene)
            scene.AddNode(self._mainGUIClass._outInitModel)

        self._mainGUIClass._outInitModel.SetAndObservePolyData(polyData)
        self._mainGUIClass._outInitModel.SetModifiedSinceRead(1)

        if self._mainGUIClass._outInitModelDisplay!=None:
            scene.RemoveNode(self._mainGUIClass._outInitModelDisplay)

        self._mainGUIClass._outInitModelDisplay = slicer.vtkMRMLModelDisplayNode()
        self._mainGUIClass._outInitModelDisplay.SetPolyData(self._mainGUIClass._outInitModel.GetPolyData())
        self._mainGUIClass._outInitModelDisplay.SetColor(0.8, 0.0, 0.0)
        self._mainGUIClass._outInitModelDisplay.SetSliceIntersectionVisibility(1)
        self._mainGUIClass._outInitModelDisplay.SetVisibility(1)
        self._mainGUIClass._outInitModelDisplay.SetOpacity(0.5)
        scene.AddNode(self._mainGUIClass._outInitModelDisplay)

        self._mainGUIClass._outInitModel.SetAndObserveDisplayNodeID(self._mainGUIClass._outInitModelDisplay.GetID())


    def GenerateEvolutionModel(self,resultContainer):

        matrix = slicer.vtkMatrix4x4()

        image = resultContainer.GetNode().GetImageData()

        resultContainer.GetNode().GetIJKToRASMatrix(matrix)
        threshold = 0.0

        polyData = slicer.vtkPolyData()

        if image.GetPointData().GetScalars():
            # marching Cubes, only if image has content
            polyData.DeepCopy(self._mainGUIClass.GetMyLogic().MarchingCubes(image,matrix,threshold))

        scene = self._mainGUIClass.GetLogic().GetMRMLScene()
        if self._mainGUIClass._outEvolModel == None:

            # no node so far
            self._mainGUIClass._outEvolModel = slicer.vtkMRMLModelNode()
            self._mainGUIClass._outEvolModel.SetName("VMTK Level-Set Evolution Output Model")
            self._mainGUIClass._outEvolModel.SetAndObservePolyData(slicer.vtkPolyData())
            self._mainGUIClass._outEvolModel.SetScene(scene)
            scene.AddNode(self._mainGUIClass._outEvolModel)

            self._mainGUIClass._outEvolModelDisplay = slicer.vtkMRMLModelDisplayNode()
            self._mainGUIClass._outEvolModelDisplay.SetColor(0.0, 0.0, 0.8)
            self._mainGUIClass._outEvolModelDisplay.SetPolyData(slicer.vtkPolyData())
            self._mainGUIClass._outEvolModelDisplay.SetVisibility(1)
            self._mainGUIClass._outEvolModelDisplay.SetOpacity(0.5)
            self._mainGUIClass._outEvolModelDisplay.SetSliceIntersectionVisibility(1)


        self._mainGUIClass._outEvolModel.SetAndObservePolyData(polyData)
        self._mainGUIClass._outEvolModel.SetModifiedSinceRead(1)
        self._mainGUIClass._outEvolModelDisplay.SetPolyData(self._mainGUIClass._outEvolModel.GetPolyData())
        self._mainGUIClass._outEvolModelDisplay.SetSliceIntersectionVisibility(1)
        self._mainGUIClass._outEvolModelDisplay.SetVisibility(1)
        self._mainGUIClass._outEvolModelDisplay.SetOpacity(0.5)
        scene.AddNode(self._mainGUIClass._outEvolModelDisplay)

        self._mainGUIClass._outEvolModel.SetAndObserveDisplayNodeID(self._mainGUIClass._outEvolModelDisplay.GetID())
        self._mainGUIClass._outEvolModelDisplay.SetSliceIntersectionVisibility(1)
        self._mainGUIClass._outEvolModelDisplay.SetVisibility(1)
        self._mainGUIClass._outEvolModelDisplay.SetOpacity(0.5)
