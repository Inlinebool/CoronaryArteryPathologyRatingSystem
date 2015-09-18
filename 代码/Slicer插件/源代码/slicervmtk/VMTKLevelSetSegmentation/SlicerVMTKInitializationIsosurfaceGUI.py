from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000
vtkKWThumbWheel_ValueChangedEvent = 10001
###
### fast marching initialization page (derived from skeleton)
###
class SlicerVMTKInitializationIsosurfaceGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._firstRowFrame = slicer.vtkKWFrame()

        self._isosurfaceLevelFrame = slicer.vtkKWFrameWithLabel()

        self._isosurfaceLevelThumbWheel = slicer.vtkKWThumbWheel()

        self._startButton = slicer.vtkKWPushButton()


        self._resetButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._firstRowFrame.SetParent(None)
        self._firstRowFrame = None
        self._isosurfaceLevelFrame.SetParent(None)
        self._isosurfaceLevelFrame = None
        self._isosurfaceLevelThumbWheel.SetParent(None)
        self._isosurfaceLevelThumbWheel = None
        self._startButton.SetParent(None)
        self._startButton = None
        self._resetButton.SetParent(None)
        self._resetButton = None

    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)
        

        node = self._parentClass.GetScriptedModuleNode()

        node.SetParameter('IS_value', self._isosurfaceLevelThumbWheel.GetValue())

    def UpdateGUI(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUI(self)

        node = self._parentClass.GetScriptedModuleNode()

        self.UpdateGUIByState()

        self._parentClass.SetUpdatingOn()
        self._isosurfaceLevelThumbWheel.SetValue(node.GetParameter("IS_value"))
        self._parentClass.SetUpdatingOff()


    # belongs to UpdateGUI
    def UpdateGUIByState(self):

        self._isosurfaceLevelFrame.AllowFrameToCollapseOff()
        self._isosurfaceLevelFrame.SetLabelText("Isosurface Level of Gray Values")
        self._isosurfaceLevelFrame.SetReliefToSunken()

        self._isosurfaceLevelThumbWheel.ClampMinimumValueOn()
        self._isosurfaceLevelThumbWheel.ClampMaximumValueOn()
        #self._isosurfaceLevelThumbWheel.ClampResolutionOn()
        self._isosurfaceLevelThumbWheel.SetLength(150)

        inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()

        if inVolumeNode:

            imageMaxValue = round(inVolumeNode.GetImageData().ToArray().max(),1)
            imageMinValue = round(inVolumeNode.GetImageData().ToArray().min(),1)
            self._parentClass.SetUpdatingOn()
            self._isosurfaceLevelThumbWheel.SetRange(imageMinValue,imageMaxValue)
            self._isosurfaceLevelThumbWheel.SetValue(round(imageMaxValue/2))
            self._parentClass.SetUpdatingOff()

        else:

            self._parentClass.SetUpdatingOn()
            self._isosurfaceLevelThumbWheel.SetRange(0,100)
            self._isosurfaceLevelThumbWheel.SetValue(15)
            self._parentClass.SetUpdatingOff()

        self._isosurfaceLevelThumbWheel.SetResolution(100)
        self._isosurfaceLevelThumbWheel.DisplayLabelOn()
        self._isosurfaceLevelThumbWheel.DisplayEntryOn()
        self._isosurfaceLevelThumbWheel.DisplayEntryAndLabelOnTopOff()
        self._isosurfaceLevelThumbWheel.GetLabel().SetText("Isosurface Level")

        self._startButton.SetEnabled(1)
        self._startButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetReliefToRaised()
        self._startButton.SetBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetText("Start!")
        self._startButton.SetHeight(2)
        self._startButton.SetWidth(8)
        self._startButton.SetBalloonHelpString("Click to start")

        self._resetButton.SetEnabled(1)
        self._resetButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetReliefToRaised()
        self._resetButton.SetBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetText("Cancel")
        self._resetButton.SetHeight(2)
        self._resetButton.SetWidth(8)
        self._resetButton.SetBalloonHelpString("Click to reset")

    def BuildGUI(self):
        self._firstRowFrame.SetParent(self._parentFrame)
        self._firstRowFrame.Create()

        self._isosurfaceLevelFrame.SetParent(self._parentFrame)
        self._isosurfaceLevelFrame.Create()

        self._isosurfaceLevelThumbWheel.SetParent(self._isosurfaceLevelFrame.GetFrame())
        self._isosurfaceLevelThumbWheel.Create()

        self._startButton.SetParent(self._parentFrame)
        self._startButton.Create()

        self._resetButton.SetParent(self._parentFrame)
        self._resetButton.Create()

        self.UpdateGUIByState()

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._firstRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))

        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._isosurfaceLevelFrame.GetWidgetName(), self._firstRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2" % (self._isosurfaceLevelThumbWheel.GetWidgetName()))

        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._startButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._resetButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
    
    def AddGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.AddGUIObservers(self)

        self._isosurfaceLevelThumbWheelTag = self._parentClass.AddObserverByNumber(self._isosurfaceLevelThumbWheel,vtkKWThumbWheel_ValueChangedEvent)

        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._resetButtonTag = self._parentClass.AddObserverByNumber(self._resetButton,vtkKWPushButton_InvokedEvent)




    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)

        self._parentClass.RemoveObserver(self._isosurfaceLevelThumbWheelTag)
        self._parentClass.RemoveObserver(self._startButtonTag)
        self._parentClass.RemoveObserver(self._resetButtonTag)




    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)
        
        if caller == self._startButton and event == vtkKWPushButton_InvokedEvent:

            self._parentClass.GetHelper().debug("StartButton clicked..")
            
            self.Execute()

        elif caller == self._resetButton and event == vtkKWPushButton_InvokedEvent:

            self._parentClass.GetHelper().debug("ResetButton clicked..")
            
            self.Reset()
        
        elif caller == self._isosurfaceLevelThumbWheel == vtkKWThumbWheel_ValueChangedEvent:

            self.UpdateMRML()



    def Execute(self):

        self._parentClass.SetUpdatingOn()

        if self._parentClass._initImageCheckbox.GetSelectedState()==1:
            inVolumeNode = self._parentClass._inVolumeSelectorSnd.GetSelected()
        else:
            inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()
        isosurfaceValue = self._isosurfaceLevelThumbWheel.GetValue()

        myLogic = self._parentClass.GetMyLogic()
        resultContainer = myLogic.ExecuteIsosurface(inVolumeNode,isosurfaceValue)
        resultContainer = self._parentClass.GetHelper().SetAndMergeInitVolume(resultContainer)
        self._parentClass.GetHelper().GenerateInitializationModel(resultContainer)

        self._parentClass.SetUpdatingOff()
        self._parentClass._state = 1
        self._parentClass.UpdateGUIByState()
        self._parentClass.UpdateMRML() # save the results


    def Reset(self):
        SlicerVMTKAdvancedPageSkeleton.Reset(self)

        self.UpdateGUIByState()



