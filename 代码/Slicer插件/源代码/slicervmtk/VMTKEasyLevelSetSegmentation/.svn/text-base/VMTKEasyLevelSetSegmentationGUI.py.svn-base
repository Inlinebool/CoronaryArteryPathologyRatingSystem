from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer

from VMTKEasyLevelSetSegmentationHelper import VMTKEasyLevelSetSegmentationHelper
from VMTKEasyLevelSetSegmentationLogic import VMTKEasyLevelSetSegmentationLogic

vtkKWPushButton_InvokedEvent = 10000
vtkKWExtent_EndChangeEvent = 10000
vtkKWRadioButton_SelectedStateChangedEvent = 10000
vtkMRMLScene_CloseEvent = 66003

vtkKWScale_ValueChangedEvent = 10001
vtkKWSpinBox_SpinBoxValueChangedEvent = 10000

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000

class VMTKEasyLevelSetSegmentationGUI(ScriptedModuleGUI):

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        #self.SetModuleName("VMTKEasyLevelSetSegmentation")
        self.SetGUIName("Easy LevelSetSegmentation using VMTK")

        self._moduleFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._moduleNodeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._moduleExistingSetsNodeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._moduleNewEntry = slicer.vtkKWEntryWithLabel()
        self._moduleNewButton = slicer.vtkKWPushButton()


        self._inVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._seedsSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._targetSeedsSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outEvolVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._vrCheckButton = slicer.vtkKWCheckButton()

        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._initFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._evolFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._sbCheckButton = slicer.vtkKWCheckButton()        
        self._thresholdExtent = slicer.vtkKWExtent()

        self._startButton = slicer.vtkKWPushButton()

        self._evolMethod  = slicer.vtkKWRadioButtonSetWithLabel()   
        self._propagationScale = slicer.vtkKWScaleWithEntry()
        self._curvatureScale = slicer.vtkKWScaleWithEntry()
        self._advectionScale = slicer.vtkKWScaleWithEntry()

        self._iterationsSpinbox = slicer.vtkKWSpinBoxWithLabel()

        self._evolStartButton = slicer.vtkKWPushButton()

        self._helper = VMTKEasyLevelSetSegmentationHelper(self)

        self._logic = VMTKEasyLevelSetSegmentationLogic(self)

        self._presetsScene = None # a new MRML Scene for the self._presetsScene environment

        self._outInitModelDisplay = None

        self._updating = 0

        self._pages = []

    def Destructor(self):

        for page in self._pages:
            page.Destructor()

        self._moduleExistingSetsNodeSelector.SetParent(None)
        self._moduleExistingSetsNodeSelector = None
        self._moduleNodeSelector.SetParent(None)
        self._moduleNodeSelector = None
        self._inVolumeSelector.SetParent(None)
        self._inVolumeSelector = None
        self._outVolumeSelector.SetParent(None)
        self._outVolumeSelector = None
        self._outEvolVolumeSelector.SetParent(None)
        self._outEvolVolumeSelector = None

        self._initFrame.SetParent(None)
        self._initFrame = None
        self._advancedTabs.SetParent(None)
        self._advancedTabs = None

        self._helper = None
        self._logic = None

    def RemoveMRMLNodeObservers(self):
        pass
    
    def RemoveLogicObservers(self):
        pass

    def AddGUIObservers(self):
        self._moduleExistingSetsNodeSelectorSelectedTag = self.AddObserverByNumber(self._moduleExistingSetsNodeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._moduleNodeSelectorSelectedTag = self.AddObserverByNumber(self._moduleNodeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._inVolumeSelectorSelectedTag = self.AddObserverByNumber(self._inVolumeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._seedsSelectorSelectedTag = self.AddObserverByNumber(self._seedsSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._targetSeedsSelectorSelectedTag = self.AddObserverByNumber(self._targetSeedsSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)

        self._thresholdExtentTag = self.AddObserverByNumber(self._thresholdExtent, vtkKWExtent_EndChangeEvent)
        self._startButtonTag = self.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._evolMethod1Tag = self.AddObserverByNumber(self._evolMethod.GetWidget().GetWidget(0),vtkKWRadioButton_SelectedStateChangedEvent)
        self._evolMethod2Tag = self.AddObserverByNumber(self._evolMethod.GetWidget().GetWidget(1),vtkKWRadioButton_SelectedStateChangedEvent)
        self._propagationScaleTag = self.AddObserverByNumber(self._propagationScale, vtkKWScale_ValueChangedEvent)
        self._curvatureScaleTag = self.AddObserverByNumber(self._curvatureScale, vtkKWScale_ValueChangedEvent)
        self._advectionScaleTag = self.AddObserverByNumber(self._advectionScale, vtkKWScale_ValueChangedEvent)
        self._iterationsSpinboxTag = self.AddObserverByNumber(self._iterationsSpinbox, vtkKWSpinBox_SpinBoxValueChangedEvent)
        self._evolStartButtonTag = self.AddObserverByNumber(self._evolStartButton,vtkKWPushButton_InvokedEvent)

    def RemoveGUIObservers(self):
        self._moduleExistingSetsNodeSelectorSelectedTag = None
        self._moduleNodeSelectorSelectedTag = None
        self._inVolumeSelectorSelectedTag = None
        self._seedsSelectorSelectedTag = None
        self._targetSeedsSelectorSelectedTag = None
        self._thresholdExtentTag = None
        self._startButtonTag = None
        self._propagationScaleTag = None
        self._curvatureScaleTag = None
        self._iterationsSpinboxTag = None
        self._evolStartButtonTag = None

    def ProcessGUIEvents(self,caller,event):
        if not self._updating:

            if caller == self._inVolumeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._inVolumeSelector.GetSelected():
                self.UpdateMRML()
                self.UpdateGUI()
            elif caller == self._outVolumeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._outVolumeSelector.GetSelected():
                self.UpdateMRML()
            elif caller == self._moduleNodeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._moduleNodeSelector.GetSelected():
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetAndObserveScriptedModuleNode(node)
                self.UpdateGUI()
            elif caller == self._moduleExistingSetsNodeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._moduleExistingSetsNodeSelector.GetSelected():
                self.UpdateGUIByPreset()
                self.UpdateMRML()
            elif caller == self._seedsSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._seedsSelector.GetSelected():
                self.SetActiveFiducialList(self._seedsSelector.GetSelected())
                self.UpdateMRML()
            elif caller == self._targetSeedsSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._targetSeedsSelector.GetSelected():
                self.SetActiveFiducialList(self._targetSeedsSelector.GetSelected())
                self.UpdateMRML()
            elif caller == self._thresholdExtent and event == vtkKWExtent_EndChangeEvent:
                self.Threshold()
                self.UpdateMRML()
            elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
                self.UpdateMRML()
                self.FM()
                self.UpdateMRML()
            elif caller == self._evolMethod.GetWidget().GetWidget(0) and event == vtkKWRadioButton_SelectedStateChangedEvent:
                self.UpdateMRML()
            elif caller == self._evolMethod.GetWidget().GetWidget(1) and event == vtkKWRadioButton_SelectedStateChangedEvent:
                self.UpdateMRML()
            elif caller == self._propagationScale and event == vtkKWScale_ValueChangedEvent:
                self.UpdateMRML()
            elif caller == self._curvatureScale and event == vtkKWScale_ValueChangedEvent:
                self.UpdateMRML()
            elif caller == self._advectionScale and event == vtkKWScale_ValueChangedEvent:
                self.UpdateMRML()
            elif caller == self._iterationsSpinbox and event == vtkKWSpinBox_SpinBoxValueChangedEvent:
                self.UpdateMRML()
            elif caller == self._evolStartButton and event == vtkKWPushButton_InvokedEvent:
                self.UpdateMRML()
                self.GAC()
                self.UpdateMRML()
            

    def SetActiveFiducialList(self,fiducialListNode):
        selectionNode = self.GetLogic().GetApplicationLogic().GetSelectionNode()
        selectionNode.SetReferenceActiveFiducialListID(fiducialListNode.GetID())

    def OnSceneClose(self):

        # scene was closed
        # reset threshold sliders
        self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
        self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)

        # delete MRML node pointers
        self._outInitModelDisplay = None

    def GAC(self):

        origVolume = self._inVolumeSelector.GetSelected()            
        segmentationVolume = self._outVolumeSelector.GetSelected()      
        outVolume = self._outEvolVolumeSelector.GetSelected() 
        seeds = self._seedsSelector.GetSelected()
        targetSeeds = self._targetSeedsSelector.GetSelected()

        vmtkFound = self.CheckForVmtkLibrary()

        if origVolume and segmentationVolume and outVolume and vmtkFound:

            numberOfIterations = int(self._iterationsSpinbox.GetWidget().GetValue())
            propagationScaling = self._propagationScale.GetValue()
            curvatureScaling = self._curvatureScale.GetValue()
            advectionScaling = self._advectionScale.GetValue()

            if (self._evolMethod.GetWidget().GetWidget(0).GetSelectedState()==1):
                result = self._logic.ExecuteGAC(origVolume.GetImageData(),segmentationVolume.GetImageData(),numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,'geodesic')
            else:
                result = self._logic.ExecuteGAC(origVolume.GetImageData(),segmentationVolume.GetImageData(),numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,'curves')

            ijkToRasMatrix = slicer.vtkMatrix4x4()
            origVolume.GetIJKToRASMatrix(ijkToRasMatrix)

            #outVolume.LabelMapOn()
            outVolume.SetAndObserveImageData(result)
            outVolume.SetIJKToRASMatrix(ijkToRasMatrix)
            outVolume.SetModifiedSinceRead(1)

            inValue = 0
            outValue = 5

            if seeds and targetSeeds:                
                if targetSeeds.GetID()!=seeds.GetID():
                    # switch thresholds for labelmap when using target points
                    inValue = 5
                    outValue = 0

            scene = self.GetLogic().GetMRMLScene()

            newDisplayNode = slicer.vtkMRMLLabelMapVolumeDisplayNode()
            newDisplayNode.SetScene(scene)
            newDisplayNode.SetDefaultColorMap()
            slicer.MRMLScene.AddNodeNoNotify(newDisplayNode)

            labelMap = slicer.vtkMRMLScalarVolumeNode()
            labelMap.SetName("VMTKEvolutionLabelMap")
            labelMap.SetAndObserveImageData(self._logic.BuildSimpleLabelMap(result,inValue,outValue))
            labelMap.SetIJKToRASMatrix(ijkToRasMatrix)
            labelMap.LabelMapOn()
            labelMap.SetAndObserveDisplayNodeID(newDisplayNode.GetID())
            scene.AddNode(labelMap)

            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveLabelVolumeID(labelMap.GetID())
            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveVolumeID(origVolume.GetID())
            slicer.ApplicationLogic.PropagateVolumeSelection()

            #slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveLabelVolumeID(outVolume.GetID())
            #slicer.ApplicationLogic.PropagateVolumeSelection()

            if self._outInitModelDisplay != None: # deactivate old init model if it exists
                #nodeId = self.GetLogic().GetMRMLScene().GetNodeByID(self._outInitModelDisplay.GetID())
                #if nodeId:
                    #if self.GetLogic().GetMRMLScene().IsNodePresent(nodeId):
                        self._helper.debug("hiding old model..")
                        self._outInitModelDisplay.SetVisibility(0)
                        self._outInitModelDisplay.SetModifiedSinceRead(1)

            if self._vrCheckButton.GetSelectedState():
                self._helper.HideVR()
                if targetSeeds:
                    self._helper.VolumeRendering(outVolume,'blue',targetSeeds.GetID()==seeds.GetID())
                else:
                    self._helper.VolumeRendering(outVolume,'blue',1)
                #self._helper.VolumeRendering(outVolume,'blue')
                self._helper.ShowVR()
            else:
                self._helper.HideVR()
                self._helper.GenerateModel(outVolume,'blue')

    def CheckForVmtkLibrary(self):

        try:
            t = slicer.vtkvmtkFastMarchingUpwindGradientImageFilter()

        except Exception:

            d = slicer.vtkKWMessageDialog()
            d.SetParent(slicer.ApplicationGUI.GetMainSlicerWindow())
            d.SetMasterWindow(slicer.ApplicationGUI.GetMainSlicerWindow())
            d.SetStyleToMessage()
            d.SetText("VmtkSlicerModule not found! Please install the VmtkSlicerModule extension to use this module!")
            d.Create()
            d.Invoke()

            return 0

        return 1

    def FM(self):
        inVolume = self._inVolumeSelector.GetSelected()
        outVolume = self._outVolumeSelector.GetSelected()
        seeds = self._seedsSelector.GetSelected()
        targetSeeds = self._targetSeedsSelector.GetSelected()

        vmtkFound = self.CheckForVmtkLibrary()

        if inVolume and outVolume and seeds and vmtkFound:

            extentValues = self._thresholdExtent.GetExtent()

            sourceSeedIds = slicer.vtkIdList()
            targetSeedIds = slicer.vtkIdList()

            image = inVolume.GetImageData()

            rasToIjkMatrix = slicer.vtkMatrix4x4()
            inVolume.GetRASToIJKMatrix(rasToIjkMatrix)


            for i in range(seeds.GetNumberOfFiducials()):
                rasPt = seeds.GetNthFiducialXYZ(i)
                rasPt.append(1)
                ijkPt = rasToIjkMatrix.MultiplyPoint(*rasPt)   
                sourceSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

            inValue = 0
            outValue = 5

            sideBranchSwitch=0
            
            if targetSeeds:
                if targetSeeds.GetID()!=seeds.GetID():

                    #only run if different fiducial lists
                    self._helper.debug("Using target points..")

                    for i in range(targetSeeds.GetNumberOfFiducials()):
                        rasPt = targetSeeds.GetNthFiducialXYZ(i)
                        rasPt.append(1)
                        ijkPt = rasToIjkMatrix.MultiplyPoint(*rasPt)
                        targetSeedIds.InsertNextId(image.ComputePointId(int(ijkPt[0]),int(ijkPt[1]),int(ijkPt[2])))

                    if self._sbCheckButton.GetSelectedState():
                        sideBranchSwitch=1 # allow side branches only if targetseeds are available

                    # switch thresholds for labelmap when using target points
                    inValue = 5
                    outValue = 0

            result = self._logic.ExecuteFM(inVolume.GetImageData(),extentValues[0],extentValues[1],sourceSeedIds,targetSeedIds,sideBranchSwitch)

            #self._helper.debug(result)

            ijkToRasMatrix = slicer.vtkMatrix4x4()
            inVolume.GetIJKToRASMatrix(ijkToRasMatrix)

            self.CreateOutVolumeNode()

            #outVolume.LabelMapOn()
            outVolume.SetAndObserveImageData(result)
            outVolume.SetIJKToRASMatrix(ijkToRasMatrix)
            outVolume.SetModifiedSinceRead(1)

            scene = self.GetLogic().GetMRMLScene()

            newDisplayNode = slicer.vtkMRMLLabelMapVolumeDisplayNode()
            newDisplayNode.SetScene(scene)
            newDisplayNode.SetDefaultColorMap()
            slicer.MRMLScene.AddNodeNoNotify(newDisplayNode)

            labelMap = slicer.vtkMRMLScalarVolumeNode()
            labelMap.SetName("VMTKInitializationLabelMap")
            labelMap.SetAndObserveImageData(self._logic.BuildSimpleLabelMap(result,inValue,outValue))
            labelMap.SetIJKToRASMatrix(ijkToRasMatrix)
            labelMap.LabelMapOn()
            labelMap.SetAndObserveDisplayNodeID(newDisplayNode.GetID())
            labelMap.SetModifiedSinceRead(1)
            scene.AddNode(labelMap)

            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveLabelVolumeID(labelMap.GetID())
            slicer.ApplicationLogic.PropagateVolumeSelection()

            displayNode = inVolume.GetDisplayNode() # reset threshold for visualization
            extentValues = self._thresholdExtent.GetExtentRange()

            displayNode.SetLowerThreshold(extentValues[0])
            displayNode.SetUpperThreshold(extentValues[1])
            displayNode.SetApplyThreshold(1)

            if self._vrCheckButton.GetSelectedState():
                self._helper.HideVR()
                if targetSeeds:
                    self._helper.VolumeRendering(outVolume,'red',targetSeeds.GetID()==seeds.GetID(),sideBranchSwitch)
                else:
                    self._helper.VolumeRendering(outVolume,'red',1)
                self._helper.ShowVR()
            else:
                self._helper.HideVR()
                self._helper.GenerateModel(outVolume,'red')

    def Threshold(self):

        self._helper.debug("Setting Threshold..")

        inVolume = self._inVolumeSelector.GetSelected()

        if inVolume:

            displayNode = inVolume.GetDisplayNode()

            extentValues = self._thresholdExtent.GetExtent()

            displayNode.SetLowerThreshold(extentValues[0])
            displayNode.SetUpperThreshold(extentValues[1])
            displayNode.SetApplyThreshold(1)

            node = self.GetScriptedModuleNode()

            if node:
                extentValues = self._thresholdExtent.GetExtent()
                node.SetParameter('LowerThreshold',extentValues[0])
                node.SetParameter('UpperThreshold',extentValues[1])

        else:

            self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
            self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)

    def CreateOutVolumeNode(self):

        if not self._outVolumeSelector.GetSelected() or self._outVolumeSelector.GetSelected()==self._inVolumeSelector.GetSelected():

            self._outVolumeSelector.SetSelectedNew("vtkMRMLScalarVolumeNode")
            self._outVolumeSelector.ProcessNewNodeCommand("vtkMRMLScalarVolumeNode", "VMTKInitializationOut")

        if not self._outEvolVolumeSelector.GetSelected() or self._outEvolVolumeSelector.GetSelected()==self._inVolumeSelector.GetSelected():

            self._outEvolVolumeSelector.SetSelectedNew("vtkMRMLScalarVolumeNode")
            self._outEvolVolumeSelector.ProcessNewNodeCommand("vtkMRMLScalarVolumeNode", "VMTKEvolutionOut")


    def UpdateMRML(self):

        if not self._updating:

            self._updating = 1

            node = self.GetScriptedModuleNode()

            if not node or not self._moduleNodeSelector.GetSelected():
                self._helper.debug("no node associated to this scriptedmodule, creating new..")
                self._moduleNodeSelector.SetSelectedNew("vtkMRMLScriptedModuleNode")
                self._moduleNodeSelector.ProcessNewNodeCommand("vtkMRMLScriptedModuleNode", "LevelSetParameters")
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetScriptedModuleNode(node)
                self._helper.debug("new node created!")

            if self._inVolumeSelector.GetSelected():
                node.SetParameter('InputVolumeRef',self._inVolumeSelector.GetSelected())
            else:
                node.SetParameter('InputVolumeRef',"None")

            if self._seedsSelector.GetSelected():
                node.SetParameter('SeedsRef',self._seedsSelector.GetSelected())
            else:
                node.SetParameter('SeedsRef',"None")

            if self._targetSeedsSelector.GetSelected():
                node.SetParameter('TargetSeedsRef',self._targetSeedsSelector.GetSelected())
            else:
                node.SetParameter('TargetSeedsRef',"None")

            if self._outVolumeSelector.GetSelected():
                node.SetParameter('OutputVolumeRef',self._outVolumeSelector.GetSelected())
            else:
                node.SetParameter('OutputVolumeRef',"None")

            if self._outEvolVolumeSelector.GetSelected():
                node.SetParameter('EvolOutputVolumeRef',self._outEvolVolumeSelector.GetSelected())
            else:
                node.SetParameter('EvolOutputVolumeRef',"None")

            '''if self._outInitModelDisplay != None:
                self._helper.debug("aaa")
                self._helper.debug(self._outInitModelDisplay.GetID())
                nodeId = self.GetLogic().GetMRMLScene().GetNodeByID(self._outInitModelDisplay.GetID())
                self._helper.debug(nodeId)
                if nodeId:
                    if self.GetLogic().GetMRMLScene().IsNodePresent(nodeId):
                        node.SetParameter('OutputInitModelDisplayRef', self._outInitModelDisplay.GetID())
                    else:
                        node.SetParameter('OutputInitModelDisplayRef', "None")
            else:
                node.SetParameter('OutputInitModelDisplayRef', "None")'''

            node.SetParameter('UseVolumeRendering',self._vrCheckButton.GetSelectedState())

            node.SetParameter('IgnoreSideBranches',self._sbCheckButton.GetSelectedState())

            node.SetParameter('EvolMethod',self._evolMethod.GetWidget().GetWidget(0).GetSelectedState())

            node.SetParameter('PropagationScale',self._propagationScale.GetValue())
            node.SetParameter('CurvatureScale',self._curvatureScale.GetValue())
            node.SetParameter('AdvectionScale',self._advectionScale.GetValue())

            node.SetParameter('Iterations',self._iterationsSpinbox.GetWidget().GetValue())

            node.SetParameter('isValidVMTKnode',"1")

            self.GetLogic().GetMRMLScene().SaveStateForUndo(node)

            node.RequestParameterList()
            self._helper.debug("parameterlist which was just set in main UpdateMRML " + node.GetParameterList())

            self._updating = 0

    def UpdateGUIByPreset(self):

        node = self._moduleExistingSetsNodeSelector.GetSelected()

        if node:

            node.RequestParameterList()
            self._helper.debug("parameterlist which was just read in main UpdateGUIByPreset " + str(node.GetParameterList()))

            if node.GetParameter('EvolMethod')==1:
                self._evolMethod.GetWidget().GetWidget(0).SetSelectedState(1);
            elif node.GetParameter('EvolMethod')==0:
                self._evolMethod.GetWidget().GetWidget(1).SetSelectedState(1);

            self._propagationScale.SetValue(node.GetParameter('PropagationScale'))
            self._curvatureScale.SetValue(node.GetParameter('CurvatureScale'))
            self._advectionScale.SetValue(node.GetParameter('AdvectionScale'))
            self._iterationsSpinbox.GetWidget().SetValue(node.GetParameter('Iterations'))

            inVolumeNode = self._inVolumeSelector.GetSelected()

            if inVolumeNode:

                # update min and max threshold
                if inVolumeNode.GetImageData():
                    scalarRange = inVolumeNode.GetImageData().GetScalarRange()
                    imageMaxValue = round(scalarRange[1],0)
                    imageMinValue = round(scalarRange[0],0)

                    lowThreshold = imageMinValue
                    upThreshold = imageMaxValue
                    changed = 0

                    if node.GetParameter('LowerThreshold'):
                        lowThreshold = node.GetParameter('LowerThreshold')
                        changed = 1

                    if node.GetParameter('UpperThreshold'):
                        upThreshold = node.GetParameter('UpperThreshold')
                        changed = 1

                    self._thresholdExtent.SetExtentRange(imageMinValue, imageMaxValue, 0, 100, 0, 100)
                    self._thresholdExtent.SetExtent(lowThreshold, upThreshold, 0, 100, 0, 100)

                    if changed:
                        self.Threshold()

                else:

                    self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
                    self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)

    def UpdateGUI(self):

        if not self._updating:

            self._updating = 1


            node = self.GetScriptedModuleNode()

            self._helper.debug("calling UpdateGUI")

            if node:

                if str(node.GetParameter('isValidVMTKnode'))=="1":

                    self._helper.debug("found valid VMTK node")

                    node.RequestParameterList()
                    self._helper.debug("parameterlist which was just read in main UpdateGUI " + str(node.GetParameterList()))

                    if node.GetParameter('InputVolumeRef')!="None":
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('InputVolumeRef')):
                            self._inVolumeSelector.SetSelected(node.GetParameter('InputVolumeRef'))
                            inVolumeNode = self._inVolumeSelector.GetSelected()

                            if inVolumeNode:

                                # update min and max threshold
                                if inVolumeNode.GetImageData():
                                    scalarRange = inVolumeNode.GetImageData().GetScalarRange()
                                    
                                    if scalarRange[1] < 1.0:
                                        imageMaxValue = scalarRange[1]
                                    else:
                                        imageMaxValue = round(scalarRange[1],0)                                                                            

                                    imageMinValue = round(scalarRange[0],0)
                                    
                                    
                                    self._thresholdExtent.SetExtentRange(imageMinValue, imageMaxValue, 0, 100, 0, 100)
                                    self._thresholdExtent.SetExtent(imageMinValue, imageMaxValue, 0, 100, 0, 100)

                                else:

                                    self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
                                    self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)

                            else:

                                self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
                                self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)

                    if node.GetParameter('SeedsRef')!="None":
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('SeedsRef')):
                            self._seedsSelector.SetSelected(node.GetParameter('SeedsRef'))

                    if node.GetParameter('TargetSeedsRef')!="None":
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('TargetSeedsRef')):
                            self._targetSeedsSelector.SetSelected(node.GetParameter('TargetSeedsRef'))

                    if node.GetParameter('OutputVolumeRef')!="None":
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('OutputVolumeRef')):
                            self._outVolumeSelector.SetSelected(node.GetParameter('OutputVolumeRef'))

                    if node.GetParameter('EvolOutputVolumeRef')!="None":
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('EvolOutputVolumeRef')):
                            self._outEvolVolumeSelector.SetSelected(node.GetParameter('EvolOutputVolumeRef'))

                    #if node.GetParameter('OutputInitModelDisplayRef')=="None" or not node.GetParameter('OutputInitModelDisplayRef'):
                        #self._outInitModelDisplay = None
                    #else:
                        #nodeId = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitModelDisplayRef'))
                        #if nodeId:
                            #if self.GetLogic().GetMRMLScene().IsNodePresent(nodeId):
                                #self._outInitModelDisplay = nodeId

                    if node.GetParameter('LowerThreshold') and node.GetParameter('UpperThreshold'):
                        self._thresholdExtent.SetExtent(node.GetParameter('LowerThreshold'), node.GetParameter('UpperThreshold'), 0, 100, 0, 100)

                    self._vrCheckButton.SetSelectedState(node.GetParameter('UseVolumeRendering'))
                    self._sbCheckButton.SetSelectedState(node.GetParameter('IgnoreSideBranches'))

                    if node.GetParameter('EvolMethod')==1:
                        self._evolMethod.GetWidget().GetWidget(0).SetSelectedState(1);
                    elif node.GetParameter('EvolMethod')==0:
                        self._evolMethod.GetWidget().GetWidget(1).SetSelectedState(1);


                    self._propagationScale.SetValue(node.GetParameter('PropagationScale'))
                    self._curvatureScale.SetValue(node.GetParameter('CurvatureScale'))
                    self._advectionScale.SetValue(node.GetParameter('AdvectionScale'))

                    self._iterationsSpinbox.GetWidget().SetValue(node.GetParameter('Iterations'))

                    self.CreateOutVolumeNode()

            self._updating = 0

    def ProcessMRMLEvents(self,caller,event):

        if caller == self.GetLogic().GetMRMLScene() and event == vtkMRMLScene_CloseEvent:
            self.OnSceneClose()

        elif caller == self.GetScriptedModuleNode():
            self.UpdateGUI()

    def LoadPresets(self):

        scriptedModuleNode = slicer.vtkMRMLScriptedModuleNode()

        self._presetsScene = slicer.vtkMRMLScene()
        self._presetsScene.RegisterNodeClass(scriptedModuleNode)

        presetFileName = str(slicer.Application.GetExtensionsInstallPath())+"/"+str(slicer.Application.GetSvnRevision())+"/"+self.GetModuleName()+"/"+self.GetModuleName()+"/presets.xml";
        self._helper.debug("presetFileName: " + presetFileName)

        self._presetsScene.SetURL(presetFileName)
        self._presetsScene.Connect()

        self._moduleExistingSetsNodeSelector.SetMRMLScene(self._presetsScene)


    def BuildGUI(self):

        self.GetUIPanel().AddPage("EasyLevelSetSegmentation","EasyLevelSetSegmentation","")
        self._vesselSegPage = self.GetUIPanel().GetPageWidget("EasyLevelSetSegmentation")
        helpText = "**Easy Level-Set Segmentation using VMTK**, developed by Daniel Haehn.\n\nAttention: This module needs the VMTK libraries which are available inside the VmtkSlicerModule extension.\n\nDocumentation and Tutorials are available at: <a>http://wiki.slicer.org/slicerWiki/index.php/Modules:VMTKEasyLevelSetSegmentation</a>\n\n**Instructions**\nwithout Parameter Sets:\n1. Select an Input Volume\n2. Place Source Seeds or select an existing Fiducial List (after selecting a Fiducial List in the Source Seeds selector, it becomes set as the active Fiducial List automatically)\n3. Optional: Place Target Seeds or select an existing Fiducial List (if Source Seeds and Target Seeds point to the same Fiducial List, Target Seeds will be ignored.) If you want to ignore sidebranches, target seeds are required!\n4. Optional: Select an Output Volume for the Initialization stage\n5. Optional: Select an Output Volume for the Evolution stage\n6. Optional: Switch between Volume Rendering or Marching Cubes as 3D Output\n7. Select an Initialization Threshold (the slice viewers show feedback)\n8. Press Start and the initial surface is overlayed in the slice viewers as a label map and shown in the 3D window\n9. Configure the behaviour of the evolving surface by using the three weight sliders\n10. Optional: Enter the number of evolution iterations\n11. Press Start and the evolved surface is overlayed in the slice viewers as a label map and shown in the 3D window\n\nwith Parameter Sets:\nPresets set the Threshold for Initialization and the Weight Sliders for Evolution. Some presets for different Use Cases exist and can be selected.\n\nEvolution functionality only:\nIf an existing segmentation (must be a binary image) should just be evolved using the Evolution stage, set the Initialization Output Volume to the existing segmentation and proceed to the Evolution Stage. The Initialization Output Volume is the input for the Evolution stage."
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer Community. See http://www.slicer.org for details."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._vesselSegPage,helpText,aboutText)

        self._helper.debug("Creating EasyLevelSetSegmentation GUI")

        self._moduleFrame.SetParent(self._vesselSegPage)
        self._moduleFrame.Create()
        self._moduleFrame.SetLabelText("VMTKEasyLevelSetSegmentation")
        self._moduleFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._moduleFrame.GetWidgetName(),self._vesselSegPage.GetWidgetName()))

        self._moduleExistingSetsNodeSelector.SetNodeClass("vtkMRMLScriptedModuleNode", "", "", "")
        self._moduleExistingSetsNodeSelector.NoneEnabledOn()
        self._moduleExistingSetsNodeSelector.ShowHiddenOn()
        self._moduleExistingSetsNodeSelector.SetParent(self._moduleFrame.GetFrame())
        self._moduleExistingSetsNodeSelector.Create()
        self._moduleExistingSetsNodeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._moduleExistingSetsNodeSelector.UpdateMenu()
        self._moduleExistingSetsNodeSelector.SetBorderWidth(2)
        self._moduleExistingSetsNodeSelector.SetLabelText("Existing Parameter Sets:")
        self._moduleExistingSetsNodeSelector.SetBalloonHelpString("select a VMTK Easy Level-Set Segmentation node with existing parameters.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._moduleExistingSetsNodeSelector.GetWidgetName())
    
        self._moduleNodeSelector.SetNodeClass("vtkMRMLScriptedModuleNode", "VMTKEasyLevelSetSegmentation", self.GetLogic().GetModuleName(), "LevelSetParameters")
        self._moduleNodeSelector.NewNodeEnabledOn()
        self._moduleNodeSelector.NoneEnabledOn()
        self._moduleNodeSelector.ShowHiddenOn()
        self._moduleNodeSelector.SetParent(self._moduleFrame.GetFrame())
        self._moduleNodeSelector.Create()
        self._moduleNodeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._moduleNodeSelector.UpdateMenu()
        self._moduleNodeSelector.SetBorderWidth(2)
        self._moduleNodeSelector.SetLabelText("Current Parameter Sets:")
        self._moduleNodeSelector.SetBalloonHelpString("select a VMTK Easy Level-Set Segmentation node from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._moduleNodeSelector.GetWidgetName())

        self._topFrame.SetParent(self._moduleFrame.GetFrame())
        self._topFrame.Create()
        self._topFrame.SetLabelText("Input/Output")
        self._topFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._topFrame.GetWidgetName())

        self._inVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","","")
        self._inVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._inVolumeSelector.Create()
        self._inVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inVolumeSelector.UpdateMenu()
        self._inVolumeSelector.SetBorderWidth(2)
        self._inVolumeSelector.SetLabelText("Input Volume: ")
        self._inVolumeSelector.SetBalloonHelpString("select an input volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._inVolumeSelector.GetWidgetName())

        self._seedsSelector.SetNodeClass("vtkMRMLFiducialListNode","","","Seeds")
        self._seedsSelector.SetParent(self._topFrame.GetFrame())
        self._seedsSelector.Create()
        self._seedsSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._seedsSelector.UpdateMenu()
        self._seedsSelector.SetNewNodeEnabled(1)
        self._seedsSelector.SetNoneEnabled(1)
        self._seedsSelector.SetBorderWidth(2)
        self._seedsSelector.SetLabelText("Source Seeds: ")
        self._seedsSelector.SetBalloonHelpString("select a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._seedsSelector.GetWidgetName())

        self._targetSeedsSelector.SetNodeClass("vtkMRMLFiducialListNode","","","Targets")
        self._targetSeedsSelector.SetParent(self._topFrame.GetFrame())
        self._targetSeedsSelector.Create()
        self._targetSeedsSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._targetSeedsSelector.UpdateMenu()
        self._targetSeedsSelector.SetNewNodeEnabled(1)
        self._targetSeedsSelector.SetNoneEnabled(1)
        self._targetSeedsSelector.SetBorderWidth(2)
        self._targetSeedsSelector.SetLabelText("Target Seeds (optional): ")
        self._targetSeedsSelector.SetBalloonHelpString("select a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._targetSeedsSelector.GetWidgetName())

        self._outVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","1","VMTKInitializationOut")
        self._outVolumeSelector.SetNewNodeEnabled(1)
        self._outVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._outVolumeSelector.Create()
        self._outVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outVolumeSelector.UpdateMenu()
        self._outVolumeSelector.SetBorderWidth(2)
        self._outVolumeSelector.SetLabelText("Initialization Output Volume: ")
        self._outVolumeSelector.SetBalloonHelpString("select an output volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outVolumeSelector.GetWidgetName())

        self._outEvolVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","1","VMTKEvolutionOut")
        self._outEvolVolumeSelector.SetNewNodeEnabled(1)
        self._outEvolVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._outEvolVolumeSelector.Create()
        self._outEvolVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outEvolVolumeSelector.UpdateMenu()
        self._outEvolVolumeSelector.SetBorderWidth(2)
        self._outEvolVolumeSelector.SetLabelText("Evolution Output Volume: ")
        self._outEvolVolumeSelector.SetBalloonHelpString("select an output volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outEvolVolumeSelector.GetWidgetName())

        self._vrCheckButton.SetParent(self._topFrame.GetFrame())
        self._vrCheckButton.Create()
        self._vrCheckButton.SetText("Use Volume Rendering")
        self._vrCheckButton.SetSelectedState(1)
        self._vrCheckButton.SetBalloonHelpString("If selected, Volume Rendering instead of a polydata Model is used to display the results.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._vrCheckButton.GetWidgetName())

        self._initFrame.SetParent(self._moduleFrame.GetFrame())
        self._initFrame.Create()
        self._initFrame.SetLabelText("Initialization")
        self._initFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._initFrame.GetWidgetName())


        self._sbCheckButton.SetParent(self._initFrame.GetFrame())
        self._sbCheckButton.Create()
        self._sbCheckButton.SetText("Ignore Side Branches")
        self._sbCheckButton.SetSelectedState(0)
        self._sbCheckButton.SetBalloonHelpString("If selected, all side branches are ignored. Target seeds are required!")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._sbCheckButton.GetWidgetName())


        self._thresholdExtent.SetParent(self._initFrame.GetFrame())
        self._thresholdExtent.Create()
        self._thresholdExtent.SetReliefToSunken()
        self._thresholdExtent.ZExtentVisibilityOff()
        self._thresholdExtent.YExtentVisibilityOff()
        self._thresholdExtent.SetEnabled(1)
        self._thresholdExtent.GetXRange().SetLabelText("Thresholding")
        self._thresholdExtent.SetExtentRange(0, 100, 0, 100, 0, 100)
        self._thresholdExtent.SetExtent(0, 100, 0, 100, 0, 100)
        self._thresholdExtent.SetBalloonHelpString("While perform thresholding on the image, the results are shown in the slice viewers.")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._thresholdExtent.GetWidgetName())

        self._startButton.SetParent(self._initFrame.GetFrame())
        self._startButton.Create()
        self._startButton.SetEnabled(1)
        self._startButton.SetText("Start !")
        self._startButton.SetBalloonHelpString("Click to start the initialization")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._startButton.GetWidgetName())

        self._evolFrame.SetParent(self._moduleFrame.GetFrame())
        self._evolFrame.Create()
        self._evolFrame.SetLabelText("Evolution")
        self._evolFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._evolFrame.GetWidgetName())

        self._evolMethod.SetParent(self._evolFrame.GetFrame())
        self._evolMethod.Create()
        self._evolMethod.SetLabelText("Method")
        v = self._evolMethod.GetWidget().AddWidget(0)
        v.SetText("Geodesic Active Contours")
        v = self._evolMethod.GetWidget().AddWidget(1)
        v.SetText("CURVES Evolution")

        self._evolMethod.GetWidget().GetWidget(0).SetSelectedState(1)

        slicer.TkCall("pack %s -side top -anchor w -expand y -padx 2 -pady 2" % self._evolMethod.GetWidgetName())


        self._propagationScale.SetParent(self._evolFrame.GetFrame())
        self._propagationScale.Create()
        self._propagationScale.SetEnabled(1)
        self._propagationScale.SetRange(-100.0,100.0)
        self._propagationScale.SetResolution(10.0)
        self._propagationScale.SetValue(0.0)
        self._propagationScale.SetLabelPositionToTop()
        self._propagationScale.SetEntryPositionToTop()
        self._propagationScale.SetLabelText("more inflation      <->      less inflation")
        self._propagationScale.SetBalloonHelpString("This controls the inflation of the evolving surface.")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 4" % self._propagationScale.GetWidgetName())

        self._curvatureScale.SetParent(self._evolFrame.GetFrame())
        self._curvatureScale.Create()
        self._curvatureScale.SetEnabled(1)
        self._curvatureScale.SetRange(-100.0,100.0)
        self._curvatureScale.SetResolution(10.0)
        self._curvatureScale.SetValue(0.0)
        self._curvatureScale.SetLabelPositionToTop()
        self._curvatureScale.SetEntryPositionToTop()
        self._curvatureScale.SetLabelText("less curvature      <->      more curvature")
        self._curvatureScale.SetBalloonHelpString("This controls the smoothness of the evolving surface.")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 4" % self._curvatureScale.GetWidgetName())

        self._advectionScale.SetParent(self._evolFrame.GetFrame())
        self._advectionScale.Create()
        self._advectionScale.SetEnabled(1)
        self._advectionScale.SetRange(-100.0,100.0)
        self._advectionScale.SetResolution(10.0)
        self._advectionScale.SetValue(0.0)
        self._advectionScale.SetLabelPositionToTop()
        self._advectionScale.SetEntryPositionToTop()
        self._advectionScale.SetLabelText("more attraction to ridges      <->      less attraction to ridges")
        self._advectionScale.SetBalloonHelpString("This controls the attraction to the gradient ridges (big gray-value differences) for the surface.")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 4" % self._advectionScale.GetWidgetName())

        self._iterationsSpinbox.SetParent(self._evolFrame.GetFrame())
        self._iterationsSpinbox.Create()
        self._iterationsSpinbox.GetWidget().SetRange(1,1000)
        self._iterationsSpinbox.GetWidget().SetIncrement(1)
        self._iterationsSpinbox.GetWidget().SetRestrictValueToInteger()
        self._iterationsSpinbox.GetWidget().SetValue(10)
        self._iterationsSpinbox.SetLabelText("Iterations: ")
        self._iterationsSpinbox.SetBalloonHelpString("Number of Iterations")
        self._iterationsSpinbox.SetBalloonHelpString("Set the number of inflations for the evolving surface.")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._iterationsSpinbox.GetWidgetName())

        self._evolStartButton.SetParent(self._evolFrame.GetFrame())
        self._evolStartButton.Create()
        self._evolStartButton.SetEnabled(1)
        self._evolStartButton.SetText("Start !")
        self._evolStartButton.SetBalloonHelpString("Click to start the evolution")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._evolStartButton.GetWidgetName())

        self.LoadPresets()

        self._helper.debug("Done Creating EasyLevelSetSegmentation GUI")


    def TearDownGUI(self):
        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("EasyLevelSetSegmentation")

    def GetOutInitModelDisplay(self):
        return self._outInitModelDisplay

    def SetOutInitModelDisplay(self,nodeId):
        self._outInitModelDisplay = nodeId

    def GetHelper(self):
        return self._helper

    def GetMyLogic(self):
        return self._logic

