from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer
import time

from SlicerVMTKLevelSetLogic import SlicerVMTKLevelSetLogic
from SlicerVMTKLevelSetGUIHelper import SlicerVMTKLevelSetGUIHelper
from SlicerVMTKInitializationWelcomeGUI import SlicerVMTKInitializationWelcomeGUI
from SlicerVMTKInitializationCollidingFrontsGUI import SlicerVMTKInitializationCollidingFrontsGUI
from SlicerVMTKInitializationFastMarchingGUI import SlicerVMTKInitializationFastMarchingGUI
from SlicerVMTKInitializationThresholdGUI import SlicerVMTKInitializationThresholdGUI
from SlicerVMTKInitializationIsosurfaceGUI import SlicerVMTKInitializationIsosurfaceGUI
from SlicerVMTKInitializationSeedsGUI import SlicerVMTKInitializationSeedsGUI
from SlicerVMTKEvolutionWelcomeGUI import SlicerVMTKEvolutionWelcomeGUI
from SlicerVMTKEvolutionGeodesicGUI import SlicerVMTKEvolutionGeodesicGUI
from SlicerVMTKEvolutionCurvesGUI import SlicerVMTKEvolutionCurvesGUI

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000
vtkKWPushButton_InvokedEvent = 10000
vtkKWCheckbox_SelectedStateChangedEvent = 10000
vtkSlicerNodeSelectorWidget_NewNodeEvent = 11001



class SlicerVMTKLevelSetGUI(ScriptedModuleGUI):

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        self.SetModuleName("Level-Set Segmentation using VMTK")
        self.SetGUIName("Level-Set Segmentation using VMTK")

        self._moduleNodeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._inVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._inVolumeSelectorSnd = slicer.vtkSlicerNodeSelectorWidget()

        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._advancedInitFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._initImageCheckbox = slicer.vtkKWCheckButton()
        self._advancedInitTabs = slicer.vtkKWNotebook()

        self._advancedInitMergeAndEndFrame = slicer.vtkKWFrame()
        self._infoLabel = slicer.vtkKWLabel()
        self._advancedInitMergeAndEndButtonSet = slicer.vtkKWPushButtonSet()

        self._advancedEvolFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._evolImageCheckbox = slicer.vtkKWCheckButton()
        self._advancedEvolTabs = slicer.vtkKWNotebook()

        self._advancedEvolUndoAndEndFrame = slicer.vtkKWFrame()
        self._advancedEvolUndoAndEndButtonSet = slicer.vtkKWPushButtonSet()

        self._helper = SlicerVMTKLevelSetGUIHelper(self)
        self._logic = SlicerVMTKLevelSetLogic(self)

        self._outInitVolume = None
        self._outInitVolumeLast = None

        self._outEvolVolume = None
        self._outEvolVolumeLast = None

        self._outInitModel = None
        self._outInitModelDisplay = None

        self._outEvolModel = None
        self._outEvolModelDisplay = None

        self._initPages = []

        self._evolPages = []

        self._updating = 0

        self._state = -1

    def Destructor(self):

        self._helper.debug("main Destructor called")

        for page in self._initPages:
            page.Destructor()

        self._moduleNodeSelector.SetParent(None)
        self._moduleNodeSelector = None
        self._inVolumeSelector.SetParent(None)
        self._inVolumeSelector = None
        self._inVolumeSelectorSnd.SetParent(None)
        self._inVolumeSelectorSnd = None

        self._topFrame.SetParent(None)
        self._topFrame = None
        self._advancedInitFrame.SetParent(None)
        self._advancedInitFrame = None
        self._advancedInitTabs.SetParent(None)
        self._advancedInitTabs = None

        self._advancedInitMergeAndEndFrame.SetParent(None)
        self._advancedInitMergeAndEndFrame = None
        self._infoLabel.SetParent(None)
        self._infoLabel = None
        self._advancedInitMergeAndEndButtonSet.SetParent(None)
        self._advancedInitMergeAndEndButtonSet = None

        self._advancedEvolFrame.SetParent(None)
        self._advancedEvolFrame = None
        self._advancedEvolTabs.SetParent(None)
        self._advancedEvolTabs = None

        self._advancedEvolUndoAndEndFrame.SetParent(None)
        self._advancedEvolUndoAndEndFrame = None
        self._advancedEvolUndoAndEndButtonSet.SetParent(None)
        self._advancedEvolUndoAndEndButtonSet = None

        self._logic = None
        self._helper = None

        self._outInitVolume = None
        self._outInitVolumeLast = None

        self._outEvolVolume = None
        self._outEvolVolumeLast = None

        self._outInitModel = None
        self._outInitModelDisplay = None

        self._outEvolModel = None
        self._outEvolModelDisplay = None

        self._initPages = None
        self._evolPages = None
        self._updating = None


    def RemoveMRMLNodeObservers(self):
        pass
    
    def RemoveLogicObservers(self):
        pass

    def AddGUIObservers(self):


        self._moduleNodeSelectorSelectedTag = self.AddObserverByNumber(self._moduleNodeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        #self._moduleNodeSelectorNewTag = self.AddObserverByNumber(self._moduleNodeSelector,vtkSlicerNodeSelectorWidget_NewNodeEvent)
        self._inVolumeSelectorSelectedTag = self.AddObserverByNumber(self._inVolumeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)


        self._advancedInitNewButtonTag = self.AddObserverByNumber(self._advancedInitNewButton,vtkKWPushButton_InvokedEvent)
        self._advancedInitRemoveLastButtonTag = self.AddObserverByNumber(self._advancedInitRemoveLastButton,vtkKWPushButton_InvokedEvent)
        self._advancedInitEndButtonTag = self.AddObserverByNumber(self._advancedInitEndButton,vtkKWPushButton_InvokedEvent)

        self._advancedEvolRemoveLastButtonTag = self.AddObserverByNumber(self._advancedEvolRemoveLastButton,vtkKWPushButton_InvokedEvent)
        self._advancedEvolEndButtonTag = self.AddObserverByNumber(self._advancedEvolEndButton,vtkKWPushButton_InvokedEvent)

        self._initImageCheckboxTag = self.AddObserverByNumber(self._initImageCheckbox,vtkKWCheckbox_SelectedStateChangedEvent)
        self._evolImageCheckboxTag = self.AddObserverByNumber(self._evolImageCheckbox,vtkKWCheckbox_SelectedStateChangedEvent)

        # observers for interaction
        self._renderWindowInteractor = slicer.ApplicationGUI.GetActiveRenderWindowInteractor()
        self._renderWindowLeftButtonReleaseTag = self._renderWindowInteractor.AddObserver("LeftButtonReleaseEvent",self._helper.HandleClickInRenderWindow)

        self._redSliceInteractor = slicer.ApplicationGUI.GetMainSliceGUI("Red").GetSliceViewer().GetRenderWidget().GetRenderWindowInteractor()
        self._redSliceLeftButtonReleaseTag = self._redSliceInteractor.AddObserver("LeftButtonReleaseEvent",self._helper.HandleClickInRedSliceWindow)

        self._yellowSliceInteractor = slicer.ApplicationGUI.GetMainSliceGUI("Yellow").GetSliceViewer().GetRenderWidget().GetRenderWindowInteractor()
        self._yellowSliceLeftButtonReleaseTag = self._yellowSliceInteractor.AddObserver("LeftButtonReleaseEvent",self._helper.HandleClickInYellowSliceWindow)

        self._greenSliceInteractor = slicer.ApplicationGUI.GetMainSliceGUI("Green").GetSliceViewer().GetRenderWidget().GetRenderWindowInteractor()
        self._greenSliceLeftButtonReleaseTag = self._greenSliceInteractor.AddObserver("LeftButtonReleaseEvent",self._helper.HandleClickInGreenSliceWindow)

        self._helper.RegisterInteractors(self._renderWindowInteractor, self._redSliceInteractor, self._yellowSliceInteractor, self._greenSliceInteractor)



        for page in self._initPages:
            page.AddGUIObservers()
        for page in self._evolPages:
            page.AddGUIObservers()

    def ProcessClickOnInitTabs(self):

        if self._updating != 1:

            self.UpdateMRML()

    def ProcessClickOnEvolTabs(self):

        if self._updating != 1:

            self.UpdateMRML()

    def RemoveGUIObservers(self):

        self.RemoveObserver(self._moduleNodeSelectorSelectedTag)
        self.RemoveObserver(self._inVolumeSelectorSelectedTag)

        self.RemoveObserver(self._advancedInitNewButtonTag)
        self.RemoveObserver(self._advancedInitRemoveLastButtonTag)
        self.RemoveObserver(self._advancedInitEndButtonTag)
        self.RemoveObserver(self._advancedEvolRemoveLastButtonTag)

        self._renderWindowInteractor.RemoveObserver(self._renderWindowLeftButtonReleaseTag)
        self._redSliceInteractor.RemoveObserver(self._redSliceLeftButtonReleaseTag)
        self._yellowSliceInteractor.RemoveObserver(self._yellowSliceLeftButtonReleaseTag)
        self._greenSliceInteractor.RemoveObserver(self._greenSliceLeftButtonReleaseTag)

        for page in self._initPages:
            page.RemoveGUIObservers()
        for page in self._evolPages:
            page.RemoveGUIObservers()

    def UpdateSelectedVolume(self):

        if self._initImageCheckbox.GetSelectedState() == 0 and self._inVolumeSelector.GetSelected():
            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveVolumeID(self._inVolumeSelector.GetSelected().GetID())
        elif self._inVolumeSelectorSnd.GetSelected():
            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveVolumeID(self._inVolumeSelectorSnd.GetSelected().GetID())

        slicer.ApplicationLogic.PropagateVolumeSelection()

    def Threshold(self,extentValues):

        inVolume = self._inVolumeSelector.GetSelected()
        displayNode = inVolume.GetDisplayNode()

        displayNode.SetLowerThreshold(extentValues[0])
        displayNode.SetUpperThreshold(extentValues[1])
        displayNode.SetApplyThreshold(1)


    def ProcessGUIEvents(self,caller,event):

        ### process events added to GUI and update MRML node

        if self._updating != 1:

            self._helper.debug("main ProcessGUIEvents called")
            
            if caller == self._inVolumeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._inVolumeSelector.GetSelected():
                self._helper.debug("inVolume node changed, calling main UpdateMRML")
                ### update the thresholdsliders
                self._state = 0
                self.UpdateMRML() # update reference to volume
                for page in self._initPages:
                    page.Reset()
                for page in self._evolPages:
                    page.Reset()
                self.UpdateMRML() # update extent values
                self.UpdateGUI()
            elif caller == self._moduleNodeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._moduleNodeSelector.GetSelected():
                self._helper.debug("parameter node changed, calling main UpdateGUI")
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetAndObserveScriptedModuleNode(node)
                self.UpdateGUI() ### scripted module node has changed, update the GUI with the values stored to the node

            elif caller == self._evolImageCheckbox and event == vtkKWCheckbox_SelectedStateChangedEvent:
                self.UpdateMRML()
            elif caller == self._initImageCheckbox and event == vtkKWCheckbox_SelectedStateChangedEvent:
                self.UpdateSelectedVolume()
                self.UpdateMRML()
            elif caller == self._advancedInitNewButton and event == vtkKWPushButton_InvokedEvent:
                self._helper.debug("Add new init Button clicked")
                self._state = 0
                for page in self._initPages:
                    page.Reset()
                self.UpdateMRML()
                self.UpdateGUIByState()
            elif caller == self._advancedInitRemoveLastButton and event == vtkKWPushButton_InvokedEvent:
                self._helper.debug("Remove last init Button clicked")
                resultContainer = self._helper.UndoInit()
                self._helper.GenerateInitializationModel(resultContainer)
                self._state = 2
                for page in self._initPages:
                    page.DeleteFiducialListsFromScene(3)
                    page.Reset()
                self.UpdateMRML()
                self.UpdateGUIByState()
            elif caller == self._advancedInitEndButton and event == vtkKWPushButton_InvokedEvent:
                self._helper.debug("Accept init Button clicked")
                self._state = 3
                for page in self._evolPages:
                    page.Reset()
                self.UpdateMRML()
                self.UpdateGUIByState()
            elif caller == self._advancedEvolRemoveLastButton and event == vtkKWPushButton_InvokedEvent:
                resultContainer = self._helper.UndoEvol()
                self._helper.GenerateEvolutionModel(resultContainer)
                self._state = 3
                for page in self._evolPages:
                    page.Reset()
                self.UpdateMRML()
                self.UpdateGUIByState()
            elif caller == self._advancedEvolEndButton and event == vtkKWPushButton_InvokedEvent:
                self._state = 0
                for page in self._initPages:
                    page.Reset()
                for page in self._evolPages:
                    page.Reset()
                self.GetLogic().GetMRMLScene().RemoveNode(self._outInitVolume)
                self.GetLogic().GetMRMLScene().RemoveNode(self._outInitVolumeLast)
                self.GetLogic().GetMRMLScene().RemoveNode(self._outInitModel)
                self.GetLogic().GetMRMLScene().RemoveNode(self._outInitModelDisplay)                
                self._outInitVolume = None
                self._outInitVolumeLast = None
                self._outInitModel = None
                self._outInitModelDisplay = None
                self.UpdateMRML()
                self.UpdateGUIByState()

            for page in self._initPages:
                page.ProcessGUIEvents(caller,event)
            for page in self._evolPages:
                page.ProcessGUIEvents(caller,event)

    def UpdateMRML(self):

        ### create the node or update all parameters from gui

        self._helper.debug("main UpdateMRML called")

        if self._updating != 1:

            node = self.GetScriptedModuleNode()
            self._updating = 1
            if not node or not self._moduleNodeSelector.GetSelected():
                self._helper.debug("no node associated to this scriptedmodule, creating new..")
                self._moduleNodeSelector.SetSelectedNew("vtkMRMLScriptedModuleNode")
                self._moduleNodeSelector.ProcessNewNodeCommand("vtkMRMLScriptedModuleNode", "VMTKParameters")
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetScriptedModuleNode(node)
                self._helper.debug("new node created!")

            if self._inVolumeSelector.GetSelected():
                node.SetParameter('InputVolumeRef',self._inVolumeSelector.GetSelected())
            else:
                node.SetParameter('InputVolumeRef',"None")


            if node.GetParameter('InputVolumeRef')=="None":
                self.UnLockInitInterface(0)
            else:
                self.UnLockInitInterface(1)

            if self._outInitVolume != None:
                node.SetParameter('OutputInitVolumeRef', self._outInitVolume.GetID())
            else:
                node.SetParameter('OutputInitVolumeRef', "None")

            if self._outInitVolumeLast != None:
                node.SetParameter('OutputInitVolumeLastRef', self._outInitVolumeLast.GetID())
            else:
                node.SetParameter('OutputInitVolumeLastRef', "None")

            if self._outEvolVolume != None:
                node.SetParameter('OutputEvolVolumeRef', self._outEvolVolume.GetID())
            else:
                node.SetParameter('OutputEvolVolumeRef', "None")

            if self._outEvolVolumeLast != None:
                node.SetParameter('OutputEvolVolumeLastRef', self._outEvolVolumeLast.GetID())
            else:
                node.SetParameter('OutputEvolVolumeLastRef', "None")

            if self._outInitModel != None:
                node.SetParameter('OutputInitModelRef', self._outInitModel.GetID())
            else:
                node.SetParameter('OutputInitModelRef', "None")

            if self._outInitModelDisplay != None:
                node.SetParameter('OutputInitModelDisplayRef', self._outInitModelDisplay.GetID())
            else:
                node.SetParameter('OutputInitModelDisplayRef', "None")

            if self._outEvolModel != None:
                node.SetParameter('OutputEvolModelRef', self._outEvolModel.GetID())
            else:
                node.SetParameter('OutputEvolModelRef', "None")

            if self._outEvolModelDisplay != None:
                node.SetParameter('OutputEvolModelDisplayRef', self._outEvolModelDisplay.GetID())
            else:
                node.SetParameter('OutputEvolModelDisplayRef', "None")

            node.SetParameter('initImageCheckbox', self._initImageCheckbox.GetSelectedState())
            node.SetParameter('evolImageCheckbox', self._evolImageCheckbox.GetSelectedState())

            ### save the current flow state
            node.SetParameter('state',self._state)

            ### save the raised tab to the node
            node.SetParameter('raisedInitializationPageID', str(self._advancedInitTabs.GetRaisedPageId()))
            node.SetParameter('raisedEvolutionPageID', str(self._advancedEvolTabs.GetRaisedPageId()))

            ### all needed values set, this is now a valid VMTKParameters node
            node.SetParameter('isValidVMTKNode',1)

            for page in self._initPages:
                page.UpdateMRML()
            for page in self._evolPages:
                page.Reset()

            node.RequestParameterList()
            self._helper.debug("parameterlist which was just set in main UpdateMRML " + node.GetParameterList())

            self.GetLogic().GetMRMLScene().SaveStateForUndo(node)


            self._updating = 0

            self._helper.debug("main UpdateMRML end")

        else:
            self._helper.debug("blocked call of UpdateMRML because updating is in progress")

    def UpdateGUI(self):


        if self._updating != 1:
            self._helper.debug("main UpdateGUI called")

            node = self.GetScriptedModuleNode()
            if node:
                
                if node.GetParameter('isValidVMTKNode'):
                    ### old node
                    ### set the values of the node into the GUI

                    
                    self._helper.debug("setting the MRML parameters to the GUI")

                    node.RequestParameterList()
                    self._helper.debug("parameterlist which was just read in main UpdateGUI " + node.GetParameterList())
                    
                    self._state = node.GetParameter('state')
                    self._helper.debug("updated state to: " + str(self._state))

                    ### select the connected inVolume
                    if node.GetParameter('InputVolumeRef')=="None":
                        self._helper.debug("no inputVolumeRef so far..")
                        self.UnLockInitInterface(0)
                        if self._inVolumeSelector.GetSelected():
                            # update input volume to current selection
                            self._helper.debug("update inputVolumeRef to the current selection")
                            self._updating = 1
                            node.SetParameter('InputVolumeRef',self._inVolumeSelector.GetSelected())
                            self._updating = 0
                            self.UnLockInitInterface(1)
                        else:
                            # no input volume at all
                            # raise first page
                            self._state = -1
                            self._updating = 1
                            node.SetParameter('raisedInitializationPageID',0)
                            node.SetParameter('raisedEvolutionPageID',0)
                            self._updating = 0
                    else:
                        ### InputVolumeRef is set, test if it points to a valid node
                        if self.GetLogic().GetMRMLScene().IsNodePresent(node.GetParameter('InputVolumeRef')):
                            self._helper.debug("inputVolumeRef is already associated, select this one in the GUI!")
                            self._updating = 1
                            self._inVolumeSelector.SetSelected(node.GetParameter('InputVolumeRef'))
                            self.UnLockInitInterface(1)
                            # update view of slice and 3d
                            slicer.ApplicationLogic.GetSelectionNode().SetReferenceActiveVolumeID(self._inVolumeSelector.GetSelected().GetID())
                            slicer.ApplicationLogic.PropagateVolumeSelection()
                            self._updating = 0
                        else:
                            self._helper.debug("inputVolumeRef points to a deleted node! update.. and lock interface")
                            self._updating = 1
                            node.SetParameter('InputVolumeRef',"None")
                            node.SetParameter('raisedInitializationPageID',0)
                            node.SetParameter('raisedEvolutionPageID',0)
                            self._updating = 0
                            self._state = -1
                            self.UnLockInitInterface(0)
                    
                    if node.GetParameter('OutputInitVolumeRef')=="None" or not node.GetParameter('OutputInitVolumeRef'):
                        self._outInitVolume = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitVolumeRef'))):
                            self._outInitVolume = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitVolumeRef'))

                    if node.GetParameter('OutputInitVolumeLastRef')=="None" or not node.GetParameter('OutputInitVolumeLastRef'):
                        self._outInitVolumeLast = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitVolumeLastRef'))):
                            self._outInitVolumeLast = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitVolumeLastRef'))

                    
                    if node.GetParameter('OutputEvolVolumeRef')=="None" or not node.GetParameter('OutputEvolVolumeRef'):
                        self._outEvolVolume = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolVolumeRef'))):
                            self._outEvolVolume = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolVolumeRef'))


                    if node.GetParameter('OutputInitModelRef')=="None" or not node.GetParameter('OutputInitModelRef'):
                        self._outInitModel = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitModelRef'))):
                            self._outInitModel = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitModelRef'))

                    if node.GetParameter('OutputInitModelDisplayRef')=="None" or not node.GetParameter('OutputInitModelDisplayRef'):
                        self._outInitModelDisplay = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitModelDisplayRef'))):
                            self._outInitModelDisplay = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputInitModelDisplayRef'))
                            #showModel?

                    if node.GetParameter('OutputEvolModelRef')=="None" or not node.GetParameter('OutputEvolModelRef'):
                        self._outEvolModel = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolModelRef'))):
                            self._outEvolModel = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolModelRef'))

                    if node.GetParameter('OutputEvolModelDisplayRef')=="None" or not node.GetParameter('OutputEvolModelDisplayRef'):
                        self._outEvolModelDisplay = None
                    else:
                        if self.GetLogic().GetMRMLScene().IsNodePresent(self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolModelDisplayRef'))):
                            self._outEvolModelDisplay = self.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter('OutputEvolModelDisplayRef'))
                            #showModel?

 

                    ### raise the correct initialization tab                
                    self._updating = 1
                    self._advancedInitTabs.RaisePage(node.GetParameter('raisedInitializationPageID'))
                    self._advancedEvolTabs.RaisePage(node.GetParameter('raisedEvolutionPageID'))
                    self._updating = 0

                    for page in self._initPages:
                        page.UpdateGUI()
                    for page in self._evolPages:
                        page.UpdateGUI()

                else:
                    # new node
                    self._helper.debug("new node, resetting the GUI and calling UpdateMRML to save the values")
                    self._advancedInitTabs.RaisePage(0)
                    self._advancedEvolTabs.RaisePage(0)
                    self._initImageCheckbox.SetSelectedState(0)
                    self._evolImageCheckbox.SetSelectedState(1)
                    self._outInitVolume = None
                    self._outInitVolumeLast = None
                    self._outEvolVolume = None
                    self._outEvolVolumeLast = None

                    self._outInitModel = None
                    self._outInitModelDisplay = None

                    self._outEvolModel = None
                    self._outEvolModelDisplay = None

                    if self._inVolumeSelector.GetSelected():
                        self._state = 0
                    else:
                        self._state = -1

                    ### reset all states
                    self.UpdateMRML()
                    for page in self._initPages:
                        page.Reset()
                    for page in self._evolPages:
                        page.Reset()
                    self.UpdateMRML() # two times MRML update because of threshold slider


                ### parameter Node changed, reset interactive mode
                self._helper.SetIsInteractiveMode(0,None)
                self._initImageCheckbox.SetSelectedState(node.GetParameter("initImageCheckbox"))
                self._evolImageCheckbox.SetSelectedState(node.GetParameter("evolImageCheckbox"))
                self.UpdateSelectedVolume() 

                self.UpdateGUIByState()

            self._helper.debug("main UpdateGUI end")

    def ProcessMRMLEvents(self,caller,event):
        if self._updating != 1:
            self._helper.debug("main ProcessMRMLEvents called, event: "+str(event))

            if caller == self.GetScriptedModuleNode() and self.GetScriptedModuleNode!=None:
                self.UpdateGUI()

    def BuildGUI(self):

        self._helper.debug("main BuildGUI called")

        self.GetUIPanel().AddPage("Level-Set Segmentation using VMTK","Level-Set Segmentation using VMTK","")
        self._vmtkLvlSetPage = self.GetUIPanel().GetPageWidget("Level-Set Segmentation using VMTK")
        helpText = "**VMTK Level-Set Segmentation in 3D Slicer**, developed by Daniel Haehn. This module uses the Vascular Modeling Toolkit (<a>http://www.vmtk.org</a>) and depends on VmtkSlicerModule.\n\nDocumentation is available here: <a>http://wiki.slicer.org/slicerWiki/index.php/Modules:VMTKLevelSetSegmentation</a>."
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer Community. See http://www.slicer.org for details."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._vmtkLvlSetPage,helpText,aboutText)

        
        self._topFrame.SetParent(self._vmtkLvlSetPage)
        self._topFrame.Create()
        self._topFrame.SetLabelText("Level-Set Segmentation Parameters")
        self._topFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._topFrame.GetWidgetName(),self._vmtkLvlSetPage.GetWidgetName()))
    
        self._moduleNodeSelector.SetNodeClass("vtkMRMLScriptedModuleNode", "ScriptedModuleName", self.GetLogic().GetModuleName(), "VMTKParameters")
        self._moduleNodeSelector.NewNodeEnabledOn()
        self._moduleNodeSelector.NoneEnabledOn()
        self._moduleNodeSelector.ShowHiddenOn()
        self._moduleNodeSelector.SetParent(self._topFrame.GetFrame())
        self._moduleNodeSelector.Create()
        self._moduleNodeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._moduleNodeSelector.UpdateMenu()
        self._moduleNodeSelector.SetBorderWidth(2)
        self._moduleNodeSelector.SetLabelText("Module Parameters:")
        self._moduleNodeSelector.SetBalloonHelpString("select a VMTK node from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._moduleNodeSelector.GetWidgetName())

        self._inVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","","")
        self._inVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._inVolumeSelector.Create()
        self._inVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inVolumeSelector.UpdateMenu()
        self._inVolumeSelector.SetBorderWidth(2)
        self._inVolumeSelector.SetLabelText("Original Volume:")
        self._inVolumeSelector.SetBalloonHelpString("select an input volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._inVolumeSelector.GetWidgetName())

        self._inVolumeSelectorSnd.SetNodeClass("vtkMRMLScalarVolumeNode","","","")
        self._inVolumeSelectorSnd.SetParent(self._topFrame.GetFrame())
        self._inVolumeSelectorSnd.Create()
        self._inVolumeSelectorSnd.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inVolumeSelectorSnd.UpdateMenu()
        self._inVolumeSelectorSnd.SetBorderWidth(2)
        self._inVolumeSelectorSnd.SetLabelText("Vessel Enhanced Volume (optional):")
        self._inVolumeSelectorSnd.SetBalloonHelpString("This optional volume can be used for initialization.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._inVolumeSelectorSnd.GetWidgetName())

        self._infoLabel.SetParent(self._vmtkLvlSetPage)
        self._infoLabel.Create()
        self._infoLabel.SetText("Choose initialization method..")
        self._infoLabel.SetImageToPredefinedIcon(20023)
        self._infoLabel.SetCompoundModeToLeft()
        self._infoLabel.SetPadX(2)
        slicer.TkCall("pack %s -side top -fill x -expand n -padx 2 -pady 2 -in %s" % (self._infoLabel.GetWidgetName(),self._vmtkLvlSetPage.GetWidgetName()))

        # initialization tabs start here
        self._advancedInitFrame.SetParent(self._vmtkLvlSetPage)
        self._advancedInitFrame.Create()
        self._advancedInitFrame.SetLabelText("Initialization")
        self._advancedInitFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._advancedInitFrame.GetWidgetName(),self._vmtkLvlSetPage.GetWidgetName()))

        self._initImageCheckbox.SetParent(self._advancedInitFrame.GetFrame())
        self._initImageCheckbox.SetText("Initialize on Vessel Enhanced Image")
        self._initImageCheckbox.SetBalloonHelpString("This could enhance the initialization step but also could result in the loss of image information.")
        self._initImageCheckbox.Create()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % (self._initImageCheckbox.GetWidgetName()))

        self._advancedInitTabs.SetParent(self._advancedInitFrame.GetFrame())
        self._advancedInitTabs.Create()
        self._advancedInitTabs.AddObserver(2089,self.ProcessClickOnInitTabs)

        self._advancedInitTabs.AddPage("Welcome","An overview of the initialization methods","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Welcome")
        self._advancedWelcomePanel = SlicerVMTKInitializationWelcomeGUI(id,self)
        self._advancedWelcomePanel.BuildGUI()
        self._initPages.append(self._advancedWelcomePanel)

        self._advancedInitTabs.AddPage("Colliding Fronts","Colliding Fronts Initialization","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Colliding Fronts")
        self._advancedCollidingFrontsPanel = SlicerVMTKInitializationCollidingFrontsGUI(id,self)
        self._advancedCollidingFrontsPanel.BuildGUI()
        self._initPages.append(self._advancedCollidingFrontsPanel)

        self._advancedInitTabs.AddPage("Fast Marching","Fast Marching Initialization","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Fast Marching")
        self._advancedFastMarchingPanel = SlicerVMTKInitializationFastMarchingGUI(id,self)
        self._advancedFastMarchingPanel.BuildGUI()
        self._initPages.append(self._advancedFastMarchingPanel)

        self._advancedInitTabs.AddPage("Isosurface","Isosurface Initialization","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Isosurface")
        self._advancedIsosurfacePanel = SlicerVMTKInitializationIsosurfaceGUI(id,self)
        self._advancedIsosurfacePanel.BuildGUI()
        self._initPages.append(self._advancedIsosurfacePanel)

        self._advancedInitTabs.AddPage("Threshold","Threshold Initialization","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Threshold")
        self._advancedThresholdPanel = SlicerVMTKInitializationThresholdGUI(id,self)
        self._advancedThresholdPanel.BuildGUI()
        self._initPages.append(self._advancedThresholdPanel)

        self._advancedInitTabs.AddPage("Seeds","Seed Initialization","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedInitTabs.GetWidgetName())
        id = self._advancedInitTabs.GetFrame("Seeds")
        self._advancedSeedsPanel = SlicerVMTKInitializationSeedsGUI(id,self)
        self._advancedSeedsPanel.BuildGUI()
        self._initPages.append(self._advancedSeedsPanel)

        # init merge and end frame
        
        self._advancedInitMergeAndEndFrame.SetParent(self._advancedInitFrame)
        self._advancedInitMergeAndEndFrame.Create()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._advancedInitMergeAndEndFrame.GetWidgetName(),self._advancedInitFrame.GetWidgetName()))

        self._advancedInitMergeAndEndButtonSet.SetParent(self._advancedInitMergeAndEndFrame)
        self._advancedInitMergeAndEndButtonSet.Create()
        self._advancedInitMergeAndEndButtonSet.SetBorderWidth(2)
        self._advancedInitMergeAndEndButtonSet.SetReliefToGroove()
        self._advancedInitMergeAndEndButtonSet.SetWidgetsPadX(1)
        self._advancedInitMergeAndEndButtonSet.SetWidgetsPadY(1)
        self._advancedInitMergeAndEndButtonSet.SetPadX(1)
        self._advancedInitMergeAndEndButtonSet.SetPadY(1)
        self._advancedInitMergeAndEndButtonSet.PackHorizontallyOn()
        self._advancedInitMergeAndEndButtonSet.ExpandWidgetsOn()
        self._advancedInitMergeAndEndButtonSet.SetMaximumNumberOfWidgetsInPackingDirection(3)

        self._advancedInitNewButton = self._advancedInitMergeAndEndButtonSet.AddWidget(0)
        self._advancedInitNewButton.Create()
        self._advancedInitNewButton.SetText("Add")
        self._advancedInitNewButton.SetImageToPredefinedIcon(20045)
        self._advancedInitNewButton.SetCompoundModeToLeft()
        self._advancedInitNewButton.SetForegroundColor(0.3,0.6,0.3)

        self._advancedInitRemoveLastButton = self._advancedInitMergeAndEndButtonSet.AddWidget(1)
        self._advancedInitRemoveLastButton.Create()
        self._advancedInitRemoveLastButton.SetText("Undo")
        self._advancedInitRemoveLastButton.SetImageToPredefinedIcon(20049)
        self._advancedInitRemoveLastButton.SetCompoundModeToLeft()
        self._advancedInitRemoveLastButton.SetForegroundColor(0.6,0.3,0.3)

        self._advancedInitEndButton = self._advancedInitMergeAndEndButtonSet.AddWidget(2)
        self._advancedInitEndButton.Create()
        self._advancedInitEndButton.SetText("Accept")
        self._advancedInitEndButton.SetImageToPredefinedIcon(20044)
        self._advancedInitEndButton.SetCompoundModeToLeft()
        self._advancedInitEndButton.SetForegroundColor(0.3,0.3,0.6)


        slicer.TkCall("pack %s -side top -fill x -expand n -padx 2 -pady 2 -in %s" % (self._advancedInitMergeAndEndButtonSet.GetWidgetName(),self._advancedInitMergeAndEndFrame.GetWidgetName()))


        # evolution tabs start here
        self._advancedEvolFrame.SetParent(self._vmtkLvlSetPage)
        self._advancedEvolFrame.Create()
        self._advancedEvolFrame.SetLabelText("Evolution")
        self._advancedEvolFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._advancedEvolFrame.GetWidgetName(),self._vmtkLvlSetPage.GetWidgetName()))

        self._evolImageCheckbox.SetParent(self._advancedEvolFrame.GetFrame())
        self._evolImageCheckbox.SetText("Evolve on Gradient Based Feature Image")
        self._evolImageCheckbox.SetBalloonHelpString("The gradient based feature image could provide a smoother evolution result but might result in the loss of image information.")
        self._evolImageCheckbox.Create()
        self._evolImageCheckbox.SetSelectedState(1)
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % (self._evolImageCheckbox.GetWidgetName()))


        self._advancedEvolTabs.SetParent(self._advancedEvolFrame.GetFrame())
        self._advancedEvolTabs.Create()
        self._advancedEvolTabs.AddObserver(2089,self.ProcessClickOnEvolTabs)

        self._advancedEvolTabs.AddPage("Welcome","An overview of the evolution methods","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedEvolTabs.GetWidgetName())
        id = self._advancedEvolTabs.GetFrame("Welcome")
        self._advancedEvolWelcomePanel = SlicerVMTKEvolutionWelcomeGUI(id,self)
        self._advancedEvolWelcomePanel.BuildGUI()
        self._evolPages.append(self._advancedEvolWelcomePanel)

        self._advancedEvolTabs.AddPage("Geodesic","Geodesic Evolution","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedEvolTabs.GetWidgetName())
        id = self._advancedEvolTabs.GetFrame("Geodesic")
        self._advancedGeodesicPanel = SlicerVMTKEvolutionGeodesicGUI(id,self)
        self._advancedGeodesicPanel.BuildGUI()
        self._evolPages.append(self._advancedGeodesicPanel)

        self._advancedEvolTabs.AddPage("Curves","Curves Evolution","")
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedEvolTabs.GetWidgetName())
        id = self._advancedEvolTabs.GetFrame("Curves")
        self._advancedCurvesPanel = SlicerVMTKEvolutionCurvesGUI(id,self)
        self._advancedCurvesPanel.BuildGUI()
        self._evolPages.append(self._advancedCurvesPanel)

        # evol undo and end frame
        
        self._advancedEvolUndoAndEndFrame.SetParent(self._advancedEvolFrame)
        self._advancedEvolUndoAndEndFrame.Create()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._advancedEvolUndoAndEndFrame.GetWidgetName(),self._advancedEvolFrame.GetWidgetName()))

        self._advancedEvolUndoAndEndButtonSet.SetParent(self._advancedEvolUndoAndEndFrame)
        self._advancedEvolUndoAndEndButtonSet.Create()
        self._advancedEvolUndoAndEndButtonSet.SetBorderWidth(2)
        self._advancedEvolUndoAndEndButtonSet.SetReliefToGroove()
        self._advancedEvolUndoAndEndButtonSet.SetWidgetsPadX(1)
        self._advancedEvolUndoAndEndButtonSet.SetWidgetsPadY(1)
        self._advancedEvolUndoAndEndButtonSet.SetPadX(1)
        self._advancedEvolUndoAndEndButtonSet.SetPadY(1)
        self._advancedEvolUndoAndEndButtonSet.PackHorizontallyOn()
        self._advancedEvolUndoAndEndButtonSet.ExpandWidgetsOn()
        self._advancedEvolUndoAndEndButtonSet.SetMaximumNumberOfWidgetsInPackingDirection(2)

        self._advancedEvolRemoveLastButton = self._advancedEvolUndoAndEndButtonSet.AddWidget(1)
        self._advancedEvolRemoveLastButton.Create()
        self._advancedEvolRemoveLastButton.SetText("Undo")
        self._advancedEvolRemoveLastButton.SetImageToPredefinedIcon(20049)
        self._advancedEvolRemoveLastButton.SetCompoundModeToLeft()
        self._advancedEvolRemoveLastButton.SetForegroundColor(0.6,0.3,0.3)

        self._advancedEvolEndButton = self._advancedEvolUndoAndEndButtonSet.AddWidget(2)
        self._advancedEvolEndButton.Create()
        self._advancedEvolEndButton.SetText("Accept")
        self._advancedEvolEndButton.SetImageToPredefinedIcon(20044)
        self._advancedEvolEndButton.SetCompoundModeToLeft()
        self._advancedEvolEndButton.SetForegroundColor(0.3,0.3,0.6)

        slicer.TkCall("pack %s -side top -fill x -expand n -padx 2 -pady 2 -in %s" % (self._advancedEvolUndoAndEndButtonSet.GetWidgetName(),self._advancedEvolUndoAndEndFrame.GetWidgetName()))



        self.UpdateGUIByState()


    def TearDownGUI(self):

        self._helper.debug("main TearDownGUI called")

        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("Level-Set Segmentation")

    def GetHelper(self):
        return self._helper

    def GetMyLogic(self):
        return self._logic

    def UnLockInitInterface(self,action):

        self._advancedInitTabs.SetEnabled(action)

    def UnLockEvolInterface(self,action):

        self._advancedEvolTabs.SetEnabled(action)



    def SetUpdatingOn(self):
        self._updating = 1

    def SetUpdatingOff(self):
        self._updating = 0

    def ChangeInfoLabel(self,text):
        self._infoLabel.SetText(text)
        self._infoLabel.SetImageToPredefinedIcon(20023)
        self._infoLabel.SetCompoundModeToLeft()


            
    # state machine for merge and init flow
    def UpdateGUIByState(self):

        self._helper.debug("Updating the GUI using state: " + str(self._state))

        self._advancedInitFrame.CollapseFrame()
        self.UnLockInitInterface(0) # lock init interface
        self._advancedInitNewButton.SetEnabled(0)
        self._advancedInitRemoveLastButton.SetEnabled(0)
        self._advancedInitEndButton.SetEnabled(0)

        self._advancedEvolFrame.CollapseFrame()
        self.UnLockEvolInterface(0) # lock evol interface
        self._advancedEvolRemoveLastButton.SetEnabled(0)
        self._advancedEvolEndButton.SetEnabled(0)

        if self._state==-1:
            # no input volume
            self.ChangeInfoLabel("Input volume needed!")


        elif self._state==0:
            # input volume valid

            self._helper.debug("mode 0")
            self.ChangeInfoLabel("Choose initialization method..")
            self._advancedInitFrame.ExpandFrame()
            self.UnLockInitInterface(1) # unlock init interface

        elif self._state==1:
            # one init done
            # collapse init tab frame
            # activate add button
            # activate undo button
            # activate finish button
            self._helper.debug("mode 1")
            self.ChangeInfoLabel("Initialization done. Add another branch?")

            self._advancedInitNewButton.SetEnabled(1)
            self._advancedInitRemoveLastButton.SetEnabled(1)
            self._advancedInitEndButton.SetEnabled(1)


        elif self._state==2:
            # undo pressed
            # dont know yet
            self._helper.debug("mode 2")
            self.ChangeInfoLabel("Undo done.")

            self._advancedInitNewButton.SetEnabled(1)
            self._advancedInitEndButton.SetEnabled(1)

        elif self._state==3:
            # finish pressed
            # enable evolution frame
            # deenable init frame
            # deenable all init buttons
            # enable all evolve buttons
            self._helper.debug("mode 3")
            self.ChangeInfoLabel("Choose evolution method..")

            self._advancedEvolFrame.ExpandFrame()
            self.UnLockEvolInterface(1) # unlock evol interface
            self._advancedEvolRemoveLastButton.SetEnabled(0)
            self._advancedEvolEndButton.SetEnabled(0)

        elif self._state == 4:
            # evolution done
            self._helper.debug("mode 4")
            self.ChangeInfoLabel("Evolution done. Accept?")
            self._advancedEvolRemoveLastButton.SetEnabled(1)
            self._advancedEvolEndButton.SetEnabled(1)


