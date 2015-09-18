from Slicer import slicer
from time import strftime
from math import floor

class VMTKEasyLevelSetSegmentationHelper(object):

    def __init__(self,parentClass):

        self._parentClass = parentClass

    def debug(self,msg):

        '''debug prints to stdout (better than print because of flush)'''

        # declaration of new variable without type specification
        debugMode = 0

        if debugMode: # debugMode is a bool

            # the print statement needs strings as input, so every value to output has to be
            # casted
            print "[VMTKEasyLevelSetSegmentation " + strftime("%H:%M:%S") + "] " + str(msg)
            import sys
            sys.stdout.flush()

    def VolumeRendering(self,volumeNode,color,flipImage=0,cf=0):

        matrix = slicer.vtkMatrix4x4()

        image = volumeNode.GetImageData()
        volumeNode.GetIJKToRASMatrix(matrix)

        scalarRange = image.GetPointData().GetScalars().GetRange()

        if color == 'red': # initialization mode
            r = 0.8
            g = 0.0
            b = 0.0

            if flipImage:
                minV = 0
                maxV = scalarRange[1]
            else:
                minV = scalarRange[0]
                maxV = 0

            if cf:
                minV = scalarRange[0]
                maxV = -0.1

        elif color == 'blue': # evolution mode
            r = 1.0
            g = 1.0
            b = 0.0

            minV = -0.4
            maxV = 0.4

        self._parentClass.GetMyLogic().VolumeRendering(image,matrix,minV,maxV,[r,g,b])

    def ShowVR(self):
        viewer = slicer.ApplicationGUI.GetActiveViewerWidget()
        viewer.GetMainViewer().AddViewProp(self._parentClass.GetMyLogic()._volume)
        viewer.RequestRender()

    def HideVR(self):
        viewer = slicer.ApplicationGUI.GetActiveViewerWidget()
        viewer.GetMainViewer().RemoveViewProp(self._parentClass.GetMyLogic()._volume)
        viewer.RequestRender()

    # color == red -> initialization
    # color == blue -> evolution
    def GenerateModel(self,volumeNode,color):

        if color == 'red':
            r = 0.8
            g = 0.0
            b = 0.0
            name = "VMTK Initialization Model"
            registerModel = 1
        elif color == 'blue':
            r = 1.0
            g = 1.0
            b = 0.0
            name = "VMTK Evolution Model"
            registerModel = 0

        matrix = slicer.vtkMatrix4x4()

        image = volumeNode.GetImageData()
        volumeNode.GetIJKToRASMatrix(matrix)

        polyData = slicer.vtkPolyData()

        if image.GetPointData().GetScalars():
            # marching Cubes, only if image has content
            polyData.DeepCopy(self._parentClass.GetMyLogic().MarchingCubes(image,matrix,0.0))
        scene = self._parentClass.GetLogic().GetMRMLScene()

        newModel = slicer.vtkMRMLModelNode()
        newModel.SetName(name)
        newModel.SetScene(scene)
        newModel.SetAndObservePolyData(polyData)
        scene.AddNode(newModel)

        newModelDisplay = slicer.vtkMRMLModelDisplayNode()
        newModelDisplay.SetPolyData(newModel.GetPolyData())
        newModelDisplay.SetColor(r, g, b)            
        newModelDisplay.SetBackfaceCulling(0)
        newModelDisplay.SetSliceIntersectionVisibility(1)
        newModelDisplay.SetVisibility(1)
        newModelDisplay.SetOpacity(1.0)
        scene.AddNode(newModelDisplay)

        newModel.SetAndObserveDisplayNodeID(newModelDisplay.GetID())

        if registerModel:
            self._parentClass.SetOutInitModelDisplay(newModelDisplay)

