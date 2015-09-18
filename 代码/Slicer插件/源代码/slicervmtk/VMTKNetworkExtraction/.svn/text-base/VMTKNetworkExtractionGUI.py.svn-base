from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer

from VMTKNetworkExtractionHelper import VMTKNetworkExtractionHelper
from VMTKNetworkExtractionLogic import VMTKNetworkExtractionLogic

vtkKWPushButton_InvokedEvent = 10000

vtkMRMLScene_CloseEvent = 66003

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000

class VMTKNetworkExtractionGUI(ScriptedModuleGUI):

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        self.SetGUIName("Network extraction using VMTK")

        self._moduleFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._inModelSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._seedsSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._outModelSelector = slicer.vtkSlicerNodeSelectorWidget()



        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._startButton = slicer.vtkKWPushButton()

        self._helper = VMTKNetworkExtractionHelper(self)

        self._logic = VMTKNetworkExtractionLogic(self)

        self._updating = 0

    def Destructor(self):



        self._helper = None
        self._logic = None

    def RemoveMRMLNodeObservers(self):
        pass
    
    def RemoveLogicObservers(self):
        pass

    def AddGUIObservers(self):


        self._startButtonTag = self.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)


    def RemoveGUIObservers(self):
        pass

    def ProcessGUIEvents(self,caller,event):
        if not self._updating:

            if caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
                self.Extract()

    def Extract(self):
        inModel = self._inModelSelector.GetSelected()
        seeds = self._seedsSelector.GetSelected()
        outModel = self._outModelSelector.GetSelected()

        vmtkFound=self.CheckForVmtkLibrary()

        if inModel and outModel and seeds and vmtkFound:

            result = slicer.vtkPolyData()
            result.DeepCopy(self._logic.extractNetwork(inModel.GetPolyData(),seeds.GetNthFiducialXYZ(0)))
            result.Update()
            outModel.SetAndObservePolyData(result)
            outModel.SetModifiedSinceRead(1)
            displayNode = outModel.GetModelDisplayNode()
            if not displayNode:
                displayNode = slicer.vtkMRMLModelDisplayNode()
            displayNode.SetPolyData(outModel.GetPolyData())
            displayNode.SetColor(0, 0, 0)
            displayNode.SetScalarVisibility(1)
            displayNode.SetActiveScalarName("Topology")
            displayNode.SetAndObserveColorNodeID(self.GetLogic().GetMRMLScene().GetNodesByName("Labels").GetItemAsObject(0).GetID())
            displayNode.SetVisibility(1)
            displayNode.SetOpacity(1.0)
            self.GetLogic().GetMRMLScene().AddNode(displayNode)

            outModel.SetAndObserveDisplayNodeID(displayNode.GetID())

            dNode = inModel.GetModelDisplayNode()
            dNode.SetOpacity(0.5)
            inModel.SetAndObserveDisplayNodeID(dNode.GetID())

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


    def UpdateMRML(self):

        if not self._updating:

            self._updating = 1

            self._updating = 0


    def UpdateGUI(self):

        if not self._updating:

            self._updating = 1

            self._updating = 0

    def ProcessMRMLEvents(self,caller,event):

        if caller == self.GetLogic().GetMRMLScene() and event == vtkMRMLScene_CloseEvent:
            self.OnSceneClose()

        elif caller == self.GetScriptedModuleNode():
            self.UpdateGUI()


    def BuildGUI(self):

        self.GetUIPanel().AddPage("NetworkExtraction","NetworkExtraction","")
        self._centerlinePage = self.GetUIPanel().GetPageWidget("NetworkExtraction")
        helpText = "**Network Extraction using VMTK**, developed by Daniel Haehn."
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer community."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._centerlinePage,helpText,aboutText)

        self._helper.debug("Creating NetworkExtraction GUI")

        self._moduleFrame.SetParent(self._centerlinePage)
        self._moduleFrame.Create()
        self._moduleFrame.SetLabelText("VMTKNetworkExtraction")
        self._moduleFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._moduleFrame.GetWidgetName(),self._centerlinePage.GetWidgetName()))

        self._topFrame.SetParent(self._moduleFrame.GetFrame())
        self._topFrame.Create()
        self._topFrame.SetLabelText("Input/Output")
        self._topFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._topFrame.GetWidgetName())

        self._inModelSelector.SetNodeClass("vtkMRMLModelNode","","","")
        self._inModelSelector.SetParent(self._topFrame.GetFrame())
        self._inModelSelector.Create()
        self._inModelSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inModelSelector.UpdateMenu()
        self._inModelSelector.SetBorderWidth(2)
        self._inModelSelector.SetLabelText("Input Model: ")
        self._inModelSelector.SetBalloonHelpString("select an input model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._inModelSelector.GetWidgetName())

        self._seedsSelector.SetNodeClass("vtkMRMLFiducialListNode","","","StartingPoint")                                                                                    
        self._seedsSelector.SetParent(self._topFrame.GetFrame())                                                                                                     
        self._seedsSelector.Create()                                                                                                                                 
        self._seedsSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())                                                                                             
        self._seedsSelector.UpdateMenu()                                                                                                                             
        self._seedsSelector.SetNewNodeEnabled(1)                                                                                                                     
        self._seedsSelector.SetNoneEnabled(0)                                                                                                                        
        self._seedsSelector.SetBorderWidth(2)                                                                                                                        
        self._seedsSelector.SetLabelText("Seed: ")                                                                                                           
        self._seedsSelector.SetBalloonHelpString("select a fiducial list")                                                                                           
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._seedsSelector.GetWidgetName()) 

        self._outModelSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKNetworkExtractionOut")
        self._outModelSelector.SetNewNodeEnabled(1)
        self._outModelSelector.SetParent(self._topFrame.GetFrame())
        self._outModelSelector.Create()
        self._outModelSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outModelSelector.UpdateMenu()
        self._outModelSelector.SetBorderWidth(2)
        self._outModelSelector.SetLabelText("Network Output Model: ")
        self._outModelSelector.SetBalloonHelpString("select an output model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outModelSelector.GetWidgetName())


        self._startButton.SetParent(self._topFrame.GetFrame())
        self._startButton.Create()
        self._startButton.SetEnabled(1)
        self._startButton.SetText("Extract Network!")
        self._startButton.SetBalloonHelpString("Click to start the network extraction")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._startButton.GetWidgetName())

        #self.CreateOutModelNodes()

        self._helper.debug("Done Creating NetworkExtraction GUI")


    def TearDownGUI(self):
        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("NetworkExtraction")

    def GetHelper(self):
        return self._helper

    def GetMyLogic(self):
        return self._logic

