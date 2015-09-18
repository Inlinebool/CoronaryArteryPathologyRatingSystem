from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000
vtkKWExtent_EndChangeEvent = 10002
vtkKWExtent_StartChangeEvent = 10000
###
### threshold initialization page (derived from skeleton)
###
class SlicerVMTKInitializationThresholdGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        #top frame starts
        self._firstRowFrame = slicer.vtkKWFrame()

        #middle frame starts
        self._secondRowFrame = slicer.vtkKWFrame()

        #threshold frame starts
        self._thresholdFrame = slicer.vtkKWFrameWithLabel()
        self._thresholdSlider = slicer.vtkKWExtent()

        self._startButton = slicer.vtkKWPushButton()
        self._resetButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._firstRowFrame.SetParent(None)
        self._firstRowFrame = None
        self._secondRowFrame.SetParent(None)
        self._secondRowFrame = None
        self._thresholdFrame.SetParent(None)
        self._thresholdFrame = None
        self._thresholdSlider.SetParent(None)
        self._thresholdSlider = None

        self._startButton.SetParent(None)
        self._startButton = None
        self._resetButton.SetParent(None)
        self._resetButton = None



    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)

        self._firstRowFrame.SetParent(self._parentFrame)
        self._firstRowFrame.Create()

        self._secondRowFrame.SetParent(self._parentFrame)
        self._secondRowFrame.Create()

        self._thresholdFrame.SetParent(self._parentFrame)
        self._thresholdFrame.Create()
     

        self._thresholdSlider.SetParent(self._thresholdFrame.GetFrame())
        self._thresholdSlider.Create()


        self._startButton.SetParent(self._parentFrame)
        self._startButton.Create()


        self._resetButton.SetParent(self._parentFrame)
        self._resetButton.Create()

        self.UpdateGUIByState()

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._firstRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._secondRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))

        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._startButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._resetButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        
        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._thresholdFrame.GetWidgetName(), self._secondRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._thresholdSlider.GetWidgetName()))



    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        extentValues = self._thresholdSlider.GetExtent()
        node.SetParameter('TH_lowerThreshold', extentValues[0])
        node.SetParameter('TH_higherThreshold', extentValues[1])

    def UpdateGUI(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUI(self)

        node = self._parentClass.GetScriptedModuleNode()
        self.UpdateGUIByState()

        self._parentClass.SetUpdatingOn()
        self._thresholdSlider.SetExtent(node.GetParameter("TH_lowerThreshold"),node.GetParameter("TH_higherThreshold"),0,100,0,100)
        self._parentClass.SetUpdatingOff()

    # belongs to UpdateGUI
    def UpdateGUIByState(self):

        self._thresholdFrame.AllowFrameToCollapseOff()
        self._thresholdFrame.SetLabelText("Threshold of Gray Values")
        self._thresholdFrame.SetReliefToSunken()


        inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()

        if inVolumeNode:

            # update min and max
            imageMaxValue = round(inVolumeNode.GetImageData().ToArray().max(),0)
            imageMinValue = round(inVolumeNode.GetImageData().ToArray().min(),0)
            self._parentClass.SetUpdatingOn()
            self._thresholdSlider.SetExtentRange(imageMinValue, imageMaxValue, 0, 100, 0, 100)
            self._thresholdSlider.SetExtent(imageMinValue, imageMaxValue, 0, 100, 0, 100)
            self._parentClass.SetUpdatingOff()

        else:

            self._parentClass.SetUpdatingOn()
            self._thresholdSlider.SetExtentRange(0, 100, 0, 100, 0, 100)
            self._thresholdSlider.SetExtent(0, 100, 0, 100, 0, 100)
            self._parentClass.SetUpdatingOff()


        self._thresholdSlider.SetReliefToSunken()        
        self._thresholdSlider.ZExtentVisibilityOff()
        self._thresholdSlider.YExtentVisibilityOff()
        self._thresholdSlider.GetXRange().SetLabelText("Gray Values of Vessels")

        self._startButton.SetEnabled(1)
        self._startButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetReliefToRaised()
        self._startButton.SetBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetText("Start!")
        self._startButton.SetWidth(8)
        self._startButton.SetHeight(2)
        self._startButton.SetBalloonHelpString("Click to start")

        self._resetButton.SetEnabled(1)
        self._resetButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetReliefToRaised()
        self._resetButton.SetBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetText("Cancel")
        self._resetButton.SetWidth(8)
        self._resetButton.SetHeight(2)
        self._resetButton.SetBalloonHelpString("Click to reset")

    def AddGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.AddGUIObservers(self)

        self._thresholdSliderTag = self._parentClass.AddObserverByNumber(self._thresholdSlider, vtkKWExtent_EndChangeEvent)
        self._thresholdSliderRealtimeTag = self._parentClass.AddObserverByNumber(self._thresholdSlider, vtkKWExtent_StartChangeEvent)
        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._resetButtonTag = self._parentClass.AddObserverByNumber(self._resetButton,vtkKWPushButton_InvokedEvent)



    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)


        self._parentClass.RemoveObserver(self._thresholdSliderTag)
        self._parentClass.RemoveObserver(self._thresholdSliderRealtimeTag)

        self._parentClass.RemoveObserver(self._startButtonTag)
        self._parentClass.RemoveObserver(self._resetButtonTag)




    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)
        

        if caller == self._startButton and event == vtkKWPushButton_InvokedEvent:

            self.Execute()
            self._parentClass.UpdateMRML()
        elif caller == self._resetButton and event == vtkKWPushButton_InvokedEvent:

            self.Reset()
            self._parentClass.UpdateMRML()
        elif caller == self._thresholdSlider and event == vtkKWExtent_EndChangeEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._thresholdSlider and event == vtkKWExtent_StartChangeEvent:
            self._parentClass.Threshold(self._thresholdSlider.GetExtent())

    def Execute(self):


        self._parentClass.SetUpdatingOn()

        extentValues = self._thresholdSlider.GetExtent()
        if self._parentClass._initImageCheckbox.GetSelectedState()==1:
            inVolumeNode = self._parentClass._inVolumeSelectorSnd.GetSelected()
        else:
            inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()
        lowerThreshold = extentValues[0]
        higherThreshold = extentValues[1]

        myLogic = self._parentClass.GetMyLogic()
        resultContainer = myLogic.ExecuteThreshold(inVolumeNode,lowerThreshold,higherThreshold)
        resultContainer = self._parentClass.GetHelper().SetAndMergeInitVolume(resultContainer)
        self._parentClass.GetHelper().GenerateInitializationModel(resultContainer)

        self._parentClass.SetUpdatingOff()
        self._parentClass._state = 1
        self._parentClass.UpdateGUIByState()
        self._parentClass.UpdateMRML() # save the results



    def Reset(self):
        SlicerVMTKAdvancedPageSkeleton.Reset(self)

        self.UpdateGUIByState()


