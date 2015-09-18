from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000
vtkKWRadioButton_SelectedStateChangedEvent = 10000
vtkKWSpinBox_ValueChangedEvent = 10000
vtkKWThumbWheel_ValueChangedEvent = 10001

class SlicerVMTKVesselEnhancementSatoGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._spinboxFrame = slicer.vtkKWFrameWithLabel()
        self._thrFrame = slicer.vtkKWFrameWithLabel()

        self._sigmaUnit  = slicer.vtkKWRadioButtonSetWithLabel()        

        self._sigmaMin = slicer.vtkKWSpinBoxWithLabel()
        self._sigmaMax = slicer.vtkKWSpinBoxWithLabel()
        self._numberOfSigmaSteps = slicer.vtkKWThumbWheel()
        self._alpha = slicer.vtkKWSpinBoxWithLabel()
        self._alpha2 = slicer.vtkKWSpinBoxWithLabel()

        self._startButton = slicer.vtkKWPushButton()

    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)


    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)


        
        self._spinboxFrame.SetParent(self._parentFrame)
        self._spinboxFrame.Create()
        self._spinboxFrame.AllowFrameToCollapseOff()
        self._spinboxFrame.SetLabelText("Tubular structure detection:")
        self._spinboxFrame.SetReliefToSunken()    

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._spinboxFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        
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
        self._numberOfSigmaSteps.GetLabel().SetText("Steps between min. and max. Diameter")
        self._numberOfSigmaSteps.SetBalloonHelpString("The discretization rate between min. and max. Diameter")

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

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._thrFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        

        self._alpha.SetParent(self._thrFrame.GetFrame())
        self._alpha.Create()
        self._alpha.GetWidget().SetRange(0.0,100.0)
        self._alpha.GetWidget().SetIncrement(0.1)
        self._alpha.GetWidget().SetWidth(5)
        self._alpha.GetWidget().SetValueFormat("%.1f")
        self._alpha.SetLabelText("Plate-like and line-like structures:")
        self._alpha.SetBalloonHelpString("This controls the sensitivity for plate-like and line-like structures.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._alpha.GetWidgetName())


        self._alpha2.SetParent(self._thrFrame.GetFrame())
        self._alpha2.Create()
        self._alpha2.GetWidget().SetRange(0.0,100.0)
        self._alpha2.GetWidget().SetIncrement(0.1)
        self._alpha2.GetWidget().SetWidth(5)
        self._alpha2.GetWidget().SetValueFormat("%.1f")
        self._alpha2.SetLabelText("Blob-like structures:")
        self._alpha2.SetBalloonHelpString("This controls the sensitivity for blob-like structures.")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._alpha2.GetWidgetName())

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
        self._alpha2Tag = self._parentClass.AddObserverByNumber(self._alpha2.GetWidget(),vtkKWSpinBox_ValueChangedEvent)


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
        elif caller == self._alpha2.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()


        elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            self.Execute()
            self._parentClass.UpdateMRML()

    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        if node:

            node.SetParameter('SATO_numberOfSigmaSteps',self._numberOfSigmaSteps.GetValue())
            node.SetParameter('SATO_usePhysicalUnits',self._sigmaUnit.GetWidget().GetWidget(0).GetSelectedState())
            node.SetParameter('SATO_sigmaMin',self._sigmaMin.GetWidget().GetValue())
            node.SetParameter('SATO_sigmaMax',self._sigmaMax.GetWidget().GetValue())
            node.SetParameter('SATO_alpha',self._alpha.GetWidget().GetValue())
            node.SetParameter('SATO_alpha2',self._alpha2.GetWidget().GetValue())

        

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

            if node.GetParameter('SATO_numberOfSigmaSteps'):
                self._numberOfSigmaSteps.SetValue(node.GetParameter('SATO_numberOfSigmaSteps'))

            if node.GetParameter('SATO_usePhysicalUnits')==1:
                self._sigmaUnit.GetWidget().GetWidget(0).SetSelectedState(1);
            elif node.GetParameter('SATO_usePhysicalUnits')==0:
                self._sigmaUnit.GetWidget().GetWidget(1).SetSelectedState(1);

            if node.GetParameter('SATO_sigmaMin'):
                self._sigmaMin.GetWidget().SetValue(node.GetParameter('SATO_sigmaMin'))

            if node.GetParameter('SATO_sigmaMax'):
                self._sigmaMax.GetWidget().SetValue(node.GetParameter('SATO_sigmaMax'))

            if node.GetParameter('SATO_alpha'):
                self._alpha.GetWidget().SetValue(node.GetParameter('SATO_alpha'))

            if node.GetParameter('SATO_alpha2'):
                self._alpha2.GetWidget().SetValue(node.GetParameter('SATO_alpha2'))

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
            slicer.Application.ErrorMessage("No input volume or no output volume found. Aborting Sato..\n")
            return
        else:

            sigmaMin = float(self._sigmaMin.GetWidget().GetValue())
            sigmaMax = float(self._sigmaMax.GetWidget().GetValue())
            numberOfSigmaSteps =  int(self._numberOfSigmaSteps.GetValue())
            alpha = float(self._alpha.GetWidget().GetValue())
            alpha2 = float(self._alpha2.GetWidget().GetValue())

            imageData = slicer.vtkImageData()
            imageData.DeepCopy(inVolume.GetImageData())
            imageData.Update()
            if (self._sigmaUnit.GetWidget().GetWidget(0).GetSelectedState()==1):
                self._parentClass.debug("use mm!")
                imageData.SetSpacing(inVolume.GetSpacing()[0], inVolume.GetSpacing()[1], inVolume.GetSpacing()[2]);

            outVolumeImage = self._parentClass._logic.ApplySatoVesselness(imageData,sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,alpha2)
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
        self._sigmaMin.GetWidget().SetValue(1.0)
        self._sigmaMax.GetWidget().SetValue(5.0)
        self._alpha.GetWidget().SetValue(0.5)
        self._alpha2.GetWidget().SetValue(2.0)

