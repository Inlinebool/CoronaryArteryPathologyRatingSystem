from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer
import random

from VMTKBranchSplittingHelper import VMTKBranchSplittingHelper
from VMTKBranchSplittingLogic import VMTKBranchSplittingLogic

vtkKWPushButton_InvokedEvent = 10000

vtkMRMLScene_CloseEvent = 66003

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000

class VMTKBranchSplittingGUI(ScriptedModuleGUI):

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        self.SetGUIName("Branch Splitting using VMTK")

        self._moduleFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._inCenterLineSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._inModelSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._outModelSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._startButton = slicer.vtkKWPushButton()
        self._checkButton = slicer.vtkKWCheckButton()

        self._helper = VMTKBranchSplittingHelper(self)

        self._logic = VMTKBranchSplittingLogic(self)

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
                self.Splitting()

    def Splitting(self):
        inCeLine = self._inCenterLineSelector.GetSelected()
        inModel = self._inModelSelector.GetSelected()
        outModel = self._outModelSelector.GetSelected()
        split = self._checkButton.GetSelectedState()

        vmtkFound=self.CheckForVmtkLibrary()

        if inCeLine and inModel and outModel and vmtkFound:

            result = slicer.vtkPolyData()
            r=self._logic.branchSplitting(inCeLine.GetPolyData(),inModel.GetPolyData())
            result.DeepCopy(r)
            result.Update()
            outModel.SetAndObservePolyData(result)
            outModel.SetModifiedSinceRead(1)
            displayNode = outModel.GetModelDisplayNode()
            if not displayNode:
                displayNode = slicer.vtkMRMLModelDisplayNode()
            displayNode.SetPolyData(outModel.GetPolyData())
            displayNode.SetColor(1, 0, 0)
            displayNode.SetScalarVisibility(1)
            displayNode.SetActiveScalarName(self._logic._GroupIdsArrayName)
            displayNode.SetAndObserveColorNodeID(self.GetLogic().GetMRMLScene().GetNodesByName("Labels").GetItemAsObject(0).GetID())
            displayNode.SetVisibility(1)
            displayNode.SetOpacity(1.0)
            self.GetLogic().GetMRMLScene().AddNode(displayNode)

            outModel.SetAndObserveDisplayNodeID(displayNode.GetID())

            dNode = inModel.GetModelDisplayNode()
            dNode.SetOpacity(0.0)
            inModel.SetAndObserveDisplayNodeID(dNode.GetID())

            if split == 1:
              ctr=0
              newPdList=self._logic.splitModels(result)
              for i in newPdList:		
                if i.GetNumberOfCells() == 0:
                  continue

                self._helper.debug("Number of Cells are: "+str(i.GetNumberOfCells()))

                ctr+=1
                scene=self.GetLogic().GetMRMLScene()

                newNode=slicer.vtkMRMLModelNode()
                newNode.SetName("VMTKBranchSplittingOut_Branch"+str(ctr))
                newNode.SetScene(scene)
                newNode.SetAndObservePolyData(i)
                scene.AddNode(newNode)

                dn=slicer.vtkMRMLModelDisplayNode()
                dn.SetPolyData(newNode.GetPolyData())
                dn.SetColor(random.random() ,random.random() ,random.random() )		    
                dn.SetBackfaceCulling(0)
                dn.SetSliceIntersectionVisibility(1)
                dn.SetVisibility(1)
                dn.SetOpacity(1.0)
                scene.AddNode(dn)
                
                newNode.SetAndObserveDisplayNodeID(dn.GetName())


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

        self.GetUIPanel().AddPage("BranchSplitting","BranchSplitting","")
        self._centerlinePage = self.GetUIPanel().GetPageWidget("BranchSplitting")
        helpText = "**Branch Splitting using VMTK**, developed by Johannes Schick."
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer community."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._centerlinePage,helpText,aboutText)

        self._helper.debug("Creating BranchSplitting GUI")

        self._moduleFrame.SetParent(self._centerlinePage)
        self._moduleFrame.Create()
        self._moduleFrame.SetLabelText("VMTKBranchSplitting")
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

        self._inCenterLineSelector.SetNodeClass("vtkMRMLModelNode","","","")
        self._inCenterLineSelector.SetParent(self._topFrame.GetFrame())
        self._inCenterLineSelector.Create()
        self._inCenterLineSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inCenterLineSelector.UpdateMenu()
        self._inCenterLineSelector.SetBorderWidth(2)
        self._inCenterLineSelector.SetLabelText("Input Centerline: ")
        self._inCenterLineSelector.SetBalloonHelpString("select an input model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._inCenterLineSelector.GetWidgetName())

        self._outModelSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKBranchSplittingOut")
        self._outModelSelector.SetNewNodeEnabled(1)
        self._outModelSelector.SetParent(self._topFrame.GetFrame())
        self._outModelSelector.Create()
        self._outModelSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outModelSelector.UpdateMenu()
        self._outModelSelector.SetBorderWidth(2)
        self._outModelSelector.SetLabelText("Branch Output Model: ")
        self._outModelSelector.SetBalloonHelpString("select an output model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outModelSelector.GetWidgetName())

        self._checkButton.SetParent(self._topFrame.GetFrame())
        self._checkButton.Create()
        self._checkButton.SetEnabled(1)
        self._checkButton.SetText("Split into models")
        self._checkButton.SetBalloonHelpString("Split model into different surface models")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._checkButton.GetWidgetName())

        self._startButton.SetParent(self._topFrame.GetFrame())
        self._startButton.Create()
        self._startButton.SetEnabled(1)
        self._startButton.SetText("Split Branchs")
        self._startButton.SetBalloonHelpString("Click to start the network extraction")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._startButton.GetWidgetName())

        #self.CreateOutModelNodes()

        self._helper.debug("Done Creating BranchSplitting GUI")


    def TearDownGUI(self):
        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("BranchSplitting")

    def GetHelper(self):
        return self._helper

    def GetMyLogic(self):
        return self._logic

