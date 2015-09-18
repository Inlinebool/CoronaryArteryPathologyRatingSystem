from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer


vtkKWPushButton_InvokedEvent = 10000
vtkKWRadioButton_SelectedStateChangedEvent = 10000
vtkKWSpinBox_ValueChangedEvent = 10000
vtkKWThumbWheel_ValueChangedEvent = 10001

class SlicerVMTKVesselEnhancementFrangiGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._spinboxFrame = slicer.vtkKWFrameWithLabel()
        self._thrFrame = slicer.vtkKWFrameWithLabel()

        self._sigmaUnit  = slicer.vtkKWRadioButtonSetWithLabel()        

        self._sigmaMin = slicer.vtkKWSpinBoxWithLabel()
        self._sigmaMax = slicer.vtkKWSpinBoxWithLabel()
        self._numberOfSigmaSteps = slicer.vtkKWThumbWheel()
        self._alpha = slicer.vtkKWSpinBoxWithLabel()
        self._beta = slicer.vtkKWSpinBoxWithLabel()
        self._gamma = slicer.vtkKWSpinBoxWithLabel()

        self._startButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)

        self._spinboxFrame.SetParent(self._parentFrame)
        self._spinboxFrame.Create()
        self._spinboxFrame.AllowFrameToCollapseOff()
        self._spinboxFrame.SetLabelText("Tubular structure detection")
        self._spinboxFrame.SetReliefToSunken()    

        #slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._spinboxFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._spinboxFrame.GetWidgetName())        

        self._numberOfSigmaSteps.SetParent(self._spinboxFrame.GetFrame())
        self._numberOfSigmaSteps.Create()
        self._numberOfSigmaSteps.SetRange(0.0,2000.0)
        self._numberOfSigmaSteps.ClampMinimumValueOn()
        self._numberOfSigmaSteps.ClampMaximumValueOn()
        self._numberOfSigmaSteps.ClampResolutionOn()
        self._numberOfSigmaSteps.SetThumbWheelHeight(10)
        self._numberOfSigmaSteps.SetResolution(1.0)
        self._numberOfSigmaSteps.SetLength(150)
        self._numberOfSigmaSteps.DisplayEntryOn()
        self._numberOfSigmaSteps.DisplayLabelOn()
        self._numberOfSigmaSteps.GetLabel().SetText("Steps between max. and min. Diameter")


        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._numberOfSigmaSteps.GetWidgetName())
        
        self._sigmaUnit.SetParent(self._spinboxFrame.GetFrame())
        self._sigmaUnit.Create()
        self._sigmaUnit.SetLabelText("Diameter specification")
        v = self._sigmaUnit.GetWidget().AddWidget(0)
        v.SetText("Physical Unit (e.g. [mm])")
        v = self._sigmaUnit.GetWidget().AddWidget(1)
        v.SetText("Voxel")

        self._sigmaUnit.GetWidget().GetWidget(0).SetSelectedState(1)

        slicer.TkCall("pack %s -side top -anchor w -expand y -padx 2 -pady 2" % self._sigmaUnit.GetWidgetName())


        self._sigmaMin.SetParent(self._spinboxFrame.GetFrame())
        self._sigmaMin.Create()
        self._sigmaMin.GetWidget().SetRange(0.0,100.0)
        self._sigmaMin.GetWidget().SetIncrement(0.1)
        self._sigmaMin.GetWidget().SetWidth(5)
        self._sigmaMin.GetWidget().SetValueFormat("%.1f")
        self._sigmaMin.SetLabelText("Min. Diameter of the Tube:")
        self._sigmaMin.SetBalloonHelpString("Select the minimal diameter of tubes to enhance.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._sigmaMin.GetWidgetName())
        
        self._sigmaMax.SetParent(self._spinboxFrame.GetFrame())
        self._sigmaMax.Create()
        self._sigmaMax.GetWidget().SetRange(0.0,100.0)
        self._sigmaMax.GetWidget().SetIncrement(0.1)
        self._sigmaMax.GetWidget().SetWidth(5)
        self._sigmaMax.GetWidget().SetValueFormat("%.1f")
        self._sigmaMax.SetLabelText("Max. Diameter of the Tube:")
        self._sigmaMax.SetBalloonHelpString("Select the maximal diameter of tubes to enhance.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._sigmaMax.GetWidgetName())


        self._thrFrame.SetParent(self._parentFrame)
        self._thrFrame.Create()
        self._thrFrame.AllowFrameToCollapseOff()
        self._thrFrame.SetLabelText("Sensitivity Thresholds:")
        self._thrFrame.SetReliefToSunken()    

        #slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._thrFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._thrFrame.GetWidgetName())

        self._alpha.SetParent(self._thrFrame.GetFrame())
        self._alpha.Create()
        self._alpha.GetWidget().SetRange(0.0,100.0)
        self._alpha.GetWidget().SetIncrement(0.1)
        self._alpha.GetWidget().SetWidth(5)
        self._alpha.GetWidget().SetValueFormat("%.1f")
        self._alpha.SetLabelText("Plate-like and line-like structures:")
        self._alpha.SetBalloonHelpString("This controls the sensitivity for plate-like and line-like structures.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._alpha.GetWidgetName())

        self._beta.SetParent(self._thrFrame.GetFrame())
        self._beta.Create()
        self._beta.GetWidget().SetRange(0.0,100.0)
        self._beta.GetWidget().SetIncrement(0.1)
        self._beta.GetWidget().SetWidth(5)
        self._beta.GetWidget().SetValueFormat("%.1f")
        self._beta.SetLabelText("Blob-like structures:")
        self._beta.SetBalloonHelpString("This controls the sensitivity for blob-like structures.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._beta.GetWidgetName())

        self._gamma.SetParent(self._thrFrame.GetFrame())
        self._gamma.Create()
        self._gamma.GetWidget().SetRange(0.0,100.0)
        self._gamma.GetWidget().SetIncrement(0.1)
        self._gamma.GetWidget().SetWidth(5)
        self._gamma.GetWidget().SetValueFormat("%.1f")
        self._gamma.SetLabelText("Contrast of image:")
        self._gamma.SetBalloonHelpString("This controls the sensitivity in terms of the contrast of the image.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._gamma.GetWidgetName())

        self._startButton.SetParent(self._parentFrame)
        self._startButton.Create()
        self._startButton.SetText("Start!")
        self._startButton.SetWidth(8)
        self._startButton.SetBalloonHelpString("Click to start")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._startButton.GetWidgetName())

        self.Reset()

    def AddGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.AddGUIObservers(self)

        self._numberOfSigmaStepsTag = self._parentClass.AddObserverByNumber(self._numberOfSigmaSteps,vtkKWThumbWheel_ValueChangedEvent)
        self._sigmaUnit1Tag = self._parentClass.AddObserverByNumber(self._sigmaUnit.GetWidget().GetWidget(0),vtkKWRadioButton_SelectedStateChangedEvent)
        self._sigmaUnit2Tag = self._parentClass.AddObserverByNumber(self._sigmaUnit.GetWidget().GetWidget(1),vtkKWRadioButton_SelectedStateChangedEvent)
        self._sigmaMinTag = self._parentClass.AddObserverByNumber(self._sigmaMin.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._sigmaMaxTag = self._parentClass.AddObserverByNumber(self._sigmaMax.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._alphaTag = self._parentClass.AddObserverByNumber(self._alpha.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._betaTag = self._parentClass.AddObserverByNumber(self._beta.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._gammaTag = self._parentClass.AddObserverByNumber(self._gamma.GetWidget(),vtkKWSpinBox_ValueChangedEvent)

        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)

        self._parentClass.RemoveObserver(self._startButtonTag)


    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)
        
        if caller == self._numberOfSigmaSteps and event == vtkKWThumbWheel_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._sigmaUnit.GetWidget().GetWidget(0) and event == vtkKWRadioButton_SelectedStateChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._sigmaUnit.GetWidget().GetWidget(1) and event == vtkKWRadioButton_SelectedStateChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._sigmaMin.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._sigmaMax.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._alpha.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._beta.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._gamma.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()

        elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            self.Execute()
            self._parentClass.UpdateMRML()

    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        if node:

            node.SetParameter('FRANGI_numberOfSigmaSteps',self._numberOfSigmaSteps.GetValue())
            node.SetParameter('FRANGI_usePhysicalUnits',self._sigmaUnit.GetWidget().GetWidget(0).GetSelectedState())
            node.SetParameter('FRANGI_sigmaMin',self._sigmaMin.GetWidget().GetValue())
            node.SetParameter('FRANGI_sigmaMax',self._sigmaMax.GetWidget().GetValue())
            node.SetParameter('FRANGI_alpha',self._alpha.GetWidget().GetValue())
            node.SetParameter('FRANGI_beta',self._beta.GetWidget().GetValue())
            node.SetParameter('FRANGI_gamma',self._gamma.GetWidget().GetValue())

    def UpdateGUI(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUI(self)


        node = self._parentClass.GetScriptedModuleNode()

        if node:

            self.UpdateGUIReal(node)

    def UpdateGUIByPreset(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUIByPreset(self)

        node = self._parentClass._moduleExistingSetsNodeSelector.GetSelected()

        if node:

            self.UpdateGUIReal(node)


    def UpdateGUIReal(self,node):

        if node:

            if node.GetParameter('FRANGI_numberOfSigmaSteps'):
                self._numberOfSigmaSteps.SetValue(node.GetParameter('FRANGI_numberOfSigmaSteps'))

            if node.GetParameter('FRANGI_usePhysicalUnits')==1:
                self._sigmaUnit.GetWidget().GetWidget(0).SetSelectedState(1);
            elif node.GetParameter('FRANGI_usePhysicalUnits')==0:
                self._sigmaUnit.GetWidget().GetWidget(1).SetSelectedState(1);

            if node.GetParameter('FRANGI_sigmaMin'):
                self._sigmaMin.GetWidget().SetValue(node.GetParameter('FRANGI_sigmaMin'))

            if node.GetParameter('FRANGI_sigmaMax'):
                self._sigmaMax.GetWidget().SetValue(node.GetParameter('FRANGI_sigmaMax'))

            if node.GetParameter('FRANGI_alpha'):
                self._alpha.GetWidget().SetValue(node.GetParameter('FRANGI_alpha'))

            if node.GetParameter('FRANGI_beta'):
                self._beta.GetWidget().SetValue(node.GetParameter('FRANGI_beta'))

            if node.GetParameter('FRANGI_gamma'):
                self._gamma.GetWidget().SetValue(node.GetParameter('FRANGI_gamma'))

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

    def Execute(self):
        SlicerVMTKAdvancedPageSkeleton.Execute(self)

        inVolume =  self._parentClass._inVolumeSelector.GetSelected()
        outVolume = self._parentClass._outVolumeSelector.GetSelected()

        if not inVolume or not outVolume or not self.CheckForVmtkLibrary():
            slicer.Application.ErrorMessage("No input volume or no output volume found. Aborting Frangi..\n")
            return
        else:

            sigmaMin = float(self._sigmaMin.GetWidget().GetValue())
            sigmaMax = float(self._sigmaMax.GetWidget().GetValue())
            numberOfSigmaSteps =  int(self._numberOfSigmaSteps.GetValue())
            alpha = float(self._alpha.GetWidget().GetValue())
            beta = float(self._beta.GetWidget().GetValue())
            gamma = float(self._gamma.GetWidget().GetValue())

            imageData = slicer.vtkImageData()
            imageData.DeepCopy(inVolume.GetImageData())
            imageData.Update()
            if (self._sigmaUnit.GetWidget().GetWidget(0).GetSelectedState()==1):
                self._parentClass.debug("use mm!")
                imageData.SetSpacing(inVolume.GetSpacing()[0], inVolume.GetSpacing()[1], inVolume.GetSpacing()[2])


            outVolumeImage = self._parentClass._logic.ApplyFrangiVesselness(imageData,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,beta,gamma)
            outVolumeImage.SetSpacing(1,1,1)

            matrix = slicer.vtkMatrix4x4()
            inVolume.GetIJKToRASMatrix(matrix)
            outVolume.SetAndObserveImageData(outVolumeImage)
            outVolume.SetIJKToRASMatrix(matrix)

            displayNode = inVolume.GetDisplayNode()
            if displayNode != None:
              newDisplayNode = displayNode.NewInstance()
              newDisplayNode.Copy(displayNode)
              slicer.MRMLScene.AddNodeNoNotify(newDisplayNode);
              outVolume.SetAndObserveDisplayNodeID(newDisplayNode.GetID())
              newDisplayNode.AutoWindowLevelOff()
              newDisplayNode.AutoWindowLevelOn() # renew auto windowlevel

            appLogic = slicer.ApplicationLogic
            selectionNode = appLogic.GetSelectionNode()
            if inVolume.GetLabelMap():
              outVolume.SetLabelMap(1)
              selectionNode.SetReferenceActiveLabelVolumeID(outVolume.GetID())
            else:
              selectionNode.SetReferenceActiveVolumeID(outVolume.GetID())
            appLogic.PropagateVolumeSelection()


    def Reset(self):
        SlicerVMTKAdvancedPageSkeleton.Reset(self)

        self._numberOfSigmaSteps.SetValue(10)
        self._sigmaUnit.GetWidget().GetWidget(0).SetSelectedState(1)
        self._sigmaMin.GetWidget().SetValue(1)
        self._sigmaMax.GetWidget().SetValue(5)
        self._alpha.GetWidget().SetValue(0.5)
        self._beta.GetWidget().SetValue(0.5)
        self._gamma.GetWidget().SetValue(5.0)

