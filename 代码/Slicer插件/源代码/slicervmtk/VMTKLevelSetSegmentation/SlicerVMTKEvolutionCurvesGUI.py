from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000

###
### curves evolution (derived from skeleton)
###
class SlicerVMTKEvolutionCurvesGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._iterationsThumbwheel = slicer.vtkKWThumbWheel()
        self._weightsFrame = slicer.vtkKWFrameWithLabel()
        self._propagationScalingSpinBox = slicer.vtkKWSpinBoxWithLabel()
        self._curvatureScalingSpinBox = slicer.vtkKWSpinBoxWithLabel()
        self._advectionScalingSpinBox = slicer.vtkKWSpinBoxWithLabel()
        self._startButton = slicer.vtkKWPushButton()
        self._resetButton = slicer.vtkKWPushButton()

    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._iterationsThumbwheel.SetParent(None)
        self._iterationsThumbwheel = None
        self._weightsFrame.SetParent(None)
        self._weightsFrame = None
        self._propagationScalingSpinBox.SetParent(None)
        self._propagationScalingSpinBox = None
        self._curvatureScalingSpinBox.SetParent(None)
        self._curvatureScalingSpinBox = None
        self._advectionScalingSpinBox.SetParent(None)
        self._advectionScalingSpinBox = None
        self._startButton.SetParent(None)
        self._startButton = None
        self._resetButton.SetParent(None)
        self._resetButton = None
    
    def AddGUIObservers(self):
        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._resetButtonTag = self._parentClass.AddObserverByNumber(self._resetButton,vtkKWPushButton_InvokedEvent)


    def RemoveGUIObservers(self):

        self._parentClass.RemoveObserver(self._startButtonTag)
        self._parentClass.RemoveObserver(self._resetButtonTag)

    def ProcessGUIEvents(self,caller,event):
        if caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            self.Execute()
            self._parentClass.UpdateMRML()
        elif caller == self._resetButton and event == vtkKWPushButton_InvokedEvent:
            self.Reset()
            self._parentClass.UpdateMRML()

    def UpdateMRML(self):
        node = self._parentClass.GetScriptedModuleNode()

        if node:

            node.SetParameter('CURVES_iterations',self._iterationsThumbwheel.GetValue())
            node.SetParameter('CURVES_propagationScaling',self._propagationScalingSpinBox.GetWidget().GetValue())
            node.SetParameter('CURVES_curvatureScaling',self._curvatureScalingSpinBox.GetWidget().GetValue())
            node.SetParameter('CURVES_advectionScaling',self._advectionScaling.GetWidget().GetValue())

    def UpdateGUI(self):

        node = self._parentClass.GetScriptedModuleNode()

        if node:

            if node.GetParameter('CURVES_iterations'):
                self._iterationsThumbwheel.SetValue(node.GetParameter('CURVES_iterations'))

            if node.GetParameter('CURVES_propagationScaling'):
                self._propagationScalingSpinBox.GetWidget().SetValue(node.GetParameter('CURVES_propagationScaling'))

            if node.GetParameter('CURVES_curvatureScaling'):
                self._curvatureScalingSpinBox.GetWidget().SetValue(node.GetParameter('CURVES_curvatureScaling'))

            if node.GetParameter('CURVES_advectionScaling'):
                self._advectionScalingSpinBox.GetWidget().SetValue(node.GetParameter('CURVES_advectionScaling'))

    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)

        self._iterationsThumbwheel.SetParent(self._parentFrame)
        self._iterationsThumbwheel.Create()
        self._iterationsThumbwheel.SetRange(0.0,2000.0)
        self._iterationsThumbwheel.ClampMinimumValueOn()
        self._iterationsThumbwheel.ClampMaximumValueOn()
        self._iterationsThumbwheel.ClampResolutionOn()
        self._iterationsThumbwheel.SetThumbWheelHeight(10)
        self._iterationsThumbwheel.SetResolution(1.0)
        self._iterationsThumbwheel.SetLength(150)
        self._iterationsThumbwheel.DisplayEntryOn()
        self._iterationsThumbwheel.DisplayLabelOn()
        #self._iterationsThumbwheel.DisplayEntryAndLabelOnTopOff()
        self._iterationsThumbwheel.GetLabel().SetText("Number of iterations")

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._iterationsThumbwheel.GetWidgetName())
        
        self._weightsFrame.SetParent(self._parentFrame)
        self._weightsFrame.Create()
        self._weightsFrame.AllowFrameToCollapseOff()
        self._weightsFrame.SetLabelText("Scaling weights:")
        self._weightsFrame.SetReliefToSunken()    

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._weightsFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        
        self._propagationScalingSpinBox.SetParent(self._weightsFrame.GetFrame())
        self._propagationScalingSpinBox.Create()
        self._propagationScalingSpinBox.GetWidget().SetRange(0.0,10.0)
        self._propagationScalingSpinBox.GetWidget().SetIncrement(0.1)
        self._propagationScalingSpinBox.GetWidget().SetWidth(5)
        self._propagationScalingSpinBox.GetWidget().SetValueFormat("%.1f")
        self._propagationScalingSpinBox.SetLabelText("Propagation scaling:")
        self._propagationScalingSpinBox.SetBalloonHelpString("Propagation scaling is the weight you assign to model inflation.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._propagationScalingSpinBox.GetWidgetName())
        
        self._curvatureScalingSpinBox.SetParent(self._weightsFrame.GetFrame())
        self._curvatureScalingSpinBox.Create()
        self._curvatureScalingSpinBox.GetWidget().SetRange(0.0,10.0)
        self._curvatureScalingSpinBox.GetWidget().SetIncrement(0.1)
        self._curvatureScalingSpinBox.GetWidget().SetWidth(5)
        self._curvatureScalingSpinBox.GetWidget().SetValueFormat("%.1f")
        self._curvatureScalingSpinBox.SetLabelText("Curvature scaling:")
        self._curvatureScalingSpinBox.SetBalloonHelpString("Curvature scaling is the weight you assign to model surface regularization (this will eventually make the model collapse and vanish if it's too strong)")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._curvatureScalingSpinBox.GetWidgetName())

        self._advectionScalingSpinBox.SetParent(self._weightsFrame.GetFrame())
        self._advectionScalingSpinBox.Create()
        self._advectionScalingSpinBox.GetWidget().SetRange(0.0,10.0)
        self._advectionScalingSpinBox.GetWidget().SetIncrement(0.1)
        self._advectionScalingSpinBox.GetWidget().SetWidth(5)
        self._advectionScalingSpinBox.GetWidget().SetValueFormat("%.1f")
        self._advectionScalingSpinBox.SetLabelText("Advection scaling:")
        self._advectionScalingSpinBox.SetBalloonHelpString("Advection scaling is the most important weight. It regulates the attraction of the surface of the image gradient modulus ridges, which is ultimately what you want.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._advectionScalingSpinBox.GetWidgetName())

        self._startButton.SetParent(self._parentFrame)
        self._startButton.Create()
        self._startButton.SetEnabled(1)
        self._startButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetReliefToRaised()
        self._startButton.SetBackgroundColor(0.9,0.9,0.9)
        self._startButton.SetText("Start!")
        self._startButton.SetWidth(8)
        self._startButton.SetHeight(2)
        self._startButton.SetBalloonHelpString("Click to start")

        self._resetButton.SetParent(self._parentFrame)
        self._resetButton.Create()
        self._resetButton.SetEnabled(1)
        self._resetButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetReliefToRaised()
        self._resetButton.SetBackgroundColor(0.9,0.9,0.9)
        self._resetButton.SetText("Cancel")
        self._resetButton.SetWidth(8)
        self._resetButton.SetHeight(2)
        self._resetButton.SetBalloonHelpString("Click to reset")


        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 5 -in %s" % (self._startButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 5 -in %s" % (self._resetButton.GetWidgetName(), self._parentFrame.GetWidgetName()))

        self.Reset()

    def Execute(self):

        scene = self._parentClass.GetLogic().GetMRMLScene()

        origInVolumeNode = self._parentClass._inVolumeSelector.GetSelected()
        inVolumeNode = self._parentClass._outInitVolume
        numberOfIterations = int(self._iterationsThumbwheel.GetValue())
        propagationScaling = float(self._propagationScalingSpinBox.GetWidget().GetValue())
        curvatureScaling = float(self._curvatureScalingSpinBox.GetWidget().GetValue())
        advectionScaling = float(self._advectionScalingSpinBox.GetWidget().GetValue())

        self._parentClass.SetUpdatingOn()

        myLogic = self._parentClass.GetMyLogic()
        resultContainer = myLogic.ExecuteCurves(origInVolumeNode,inVolumeNode,numberOfIterations,propagationScaling,curvatureScaling,advectionScaling,self._parentClass._evolImageCheckbox.GetSelectedState())
        resultContainer = self._parentClass.GetHelper().SetAndMergeEvolVolume(resultContainer)
        self._parentClass.GetHelper().GenerateEvolutionModel(resultContainer)

        self._parentClass.SetUpdatingOff()

        self._parentClass._state = 4
        self._parentClass.UpdateGUIByState()
        self._parentClass.UpdateMRML() # save the results

    def Reset(self):

        self._iterationsThumbwheel.SetValue(300)
        self._propagationScalingSpinBox.GetWidget().SetValue(0.0)
        self._curvatureScalingSpinBox.GetWidget().SetValue(0.0)
        self._advectionScalingSpinBox.GetWidget().SetValue(1.0)

