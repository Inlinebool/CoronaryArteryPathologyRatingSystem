# -*- coding: utf-8 -*-
from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000
vtkKWSpinBox_ValueChangedEvent = 10000
vtkKWThumbWheel_ValueChangedEvent = 10001

class SlicerVMTKVesselEnhancementVEDMGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._spinboxFrame = slicer.vtkKWFrameWithLabel()

        self._sigmaMin = slicer.vtkKWSpinBoxWithLabel()
        self._sigmaMax = slicer.vtkKWSpinBoxWithLabel()
        self._numberOfSigmaSteps = slicer.vtkKWThumbWheel()
        self._alpha = slicer.vtkKWSpinBoxWithLabel()
        self._beta = slicer.vtkKWSpinBoxWithLabel()
        self._gamma = slicer.vtkKWSpinBoxWithLabel()
        self._timestep = slicer.vtkKWSpinBoxWithLabel()
        self._epsilon = slicer.vtkKWSpinBoxWithLabel()
        self._wstrength = slicer.vtkKWSpinBoxWithLabel()
        self._sensitivity = slicer.vtkKWSpinBoxWithLabel()
        self._numberOfIterations = slicer.vtkKWThumbWheel()
        self._numberOfDiffusionSubIterations = slicer.vtkKWThumbWheel()

        self._startButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)


    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)


        self._numberOfSigmaSteps.SetParent(self._parentFrame)
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
        self._numberOfSigmaSteps.GetLabel().SetText("Number of Sigma Steps")


        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._numberOfSigmaSteps.GetWidgetName())
        
        self._numberOfIterations.SetParent(self._parentFrame)
        self._numberOfIterations.Create()
        self._numberOfIterations.SetRange(0.0,2000.0)
        self._numberOfIterations.ClampMinimumValueOn()
        self._numberOfIterations.ClampMaximumValueOn()
        self._numberOfIterations.ClampResolutionOn()
        self._numberOfIterations.SetThumbWheelHeight(10)
        self._numberOfIterations.SetResolution(1.0)
        self._numberOfIterations.SetLength(150)
        self._numberOfIterations.DisplayEntryOn()
        self._numberOfIterations.DisplayLabelOn()
        self._numberOfIterations.GetLabel().SetText("Number of Iterations")


        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._numberOfIterations.GetWidgetName())

        self._numberOfDiffusionSubIterations.SetParent(self._parentFrame)
        self._numberOfDiffusionSubIterations.Create()
        self._numberOfDiffusionSubIterations.SetRange(0.0,2000.0)
        self._numberOfDiffusionSubIterations.ClampMinimumValueOn()
        self._numberOfDiffusionSubIterations.ClampMaximumValueOn()
        self._numberOfDiffusionSubIterations.ClampResolutionOn()
        self._numberOfDiffusionSubIterations.SetThumbWheelHeight(10)
        self._numberOfDiffusionSubIterations.SetResolution(1.0)
        self._numberOfDiffusionSubIterations.SetLength(150)
        self._numberOfDiffusionSubIterations.DisplayEntryOn()
        self._numberOfDiffusionSubIterations.DisplayLabelOn()
        self._numberOfDiffusionSubIterations.GetLabel().SetText("Number of Diffusion Sub Iterations")


        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10" % self._numberOfDiffusionSubIterations.GetWidgetName())

        self._spinboxFrame.SetParent(self._parentFrame)
        self._spinboxFrame.Create()
        self._spinboxFrame.AllowFrameToCollapseOff()
        self._spinboxFrame.SetLabelText("Input arguments")
        self._spinboxFrame.SetReliefToSunken()    

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 10 -in %s" % (self._spinboxFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        
        self._sigmaMin.SetParent(self._spinboxFrame.GetFrame())
        self._sigmaMin.Create()
        self._sigmaMin.GetWidget().SetRange(0.0,100.0)
        self._sigmaMin.GetWidget().SetIncrement(0.1)
        self._sigmaMin.GetWidget().SetWidth(5)
        self._sigmaMin.GetWidget().SetValueFormat("%.1f")
        self._sigmaMin.SetLabelText("Sigma Min:")
        self._sigmaMin.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._sigmaMin.GetWidgetName())
        
        self._sigmaMax.SetParent(self._spinboxFrame.GetFrame())
        self._sigmaMax.Create()
        self._sigmaMax.GetWidget().SetRange(0.0,100.0)
        self._sigmaMax.GetWidget().SetIncrement(0.1)
        self._sigmaMax.GetWidget().SetWidth(5)
        self._sigmaMax.GetWidget().SetValueFormat("%.1f")
        self._sigmaMax.SetLabelText("Sigma Max:")
        self._sigmaMax.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._sigmaMax.GetWidgetName())

        self._alpha.SetParent(self._spinboxFrame.GetFrame())
        self._alpha.Create()
        self._alpha.GetWidget().SetRange(0.0,100.0)
        self._alpha.GetWidget().SetIncrement(0.1)
        self._alpha.GetWidget().SetWidth(5)
        self._alpha.GetWidget().SetValueFormat("%.1f")
        self._alpha.SetLabelText("Alpha:")
        self._alpha.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._alpha.GetWidgetName())

        self._beta.SetParent(self._spinboxFrame.GetFrame())
        self._beta.Create()
        self._beta.GetWidget().SetRange(0.0,100.0)
        self._beta.GetWidget().SetIncrement(0.1)
        self._beta.GetWidget().SetWidth(5)
        self._beta.GetWidget().SetValueFormat("%.1f")
        self._beta.SetLabelText("Beta:")
        self._beta.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._beta.GetWidgetName())

        self._gamma.SetParent(self._spinboxFrame.GetFrame())
        self._gamma.Create()
        self._gamma.GetWidget().SetRange(0.0,100.0)
        self._gamma.GetWidget().SetIncrement(0.1)
        self._gamma.GetWidget().SetWidth(5)
        self._gamma.GetWidget().SetValueFormat("%.1f")
        self._gamma.SetLabelText("Gamma:")
        self._gamma.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._gamma.GetWidgetName())

        self._timestep.SetParent(self._spinboxFrame.GetFrame())
        self._timestep.Create()
        self._timestep.GetWidget().SetRange(0.0,100.0)
        self._timestep.GetWidget().SetIncrement(0.01)
        self._timestep.GetWidget().SetWidth(5)
        self._timestep.GetWidget().SetValueFormat("%.2f")
        self._timestep.SetLabelText("Timestep:")
        self._timestep.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._timestep.GetWidgetName())

        self._epsilon.SetParent(self._spinboxFrame.GetFrame())
        self._epsilon.Create()
        self._epsilon.GetWidget().SetRange(0.0,100.0)
        self._epsilon.GetWidget().SetIncrement(0.01)
        self._epsilon.GetWidget().SetWidth(5)
        self._epsilon.GetWidget().SetValueFormat("%.2f")
        self._epsilon.SetLabelText("Epsilon:")
        self._epsilon.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._epsilon.GetWidgetName())

        self._wstrength.SetParent(self._spinboxFrame.GetFrame())
        self._wstrength.Create()
        self._wstrength.GetWidget().SetRange(0.0,100.0)
        self._wstrength.GetWidget().SetIncrement(0.1)
        self._wstrength.GetWidget().SetWidth(5)
        self._wstrength.GetWidget().SetValueFormat("%.1f")
        self._wstrength.SetLabelText("WStrength:")
        self._wstrength.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._wstrength.GetWidgetName())

        self._sensitivity.SetParent(self._spinboxFrame.GetFrame())
        self._sensitivity.Create()
        self._sensitivity.GetWidget().SetRange(0.0,100.0)
        self._sensitivity.GetWidget().SetIncrement(0.1)
        self._sensitivity.GetWidget().SetWidth(5)
        self._sensitivity.GetWidget().SetValueFormat("%.1f")
        self._sensitivity.SetLabelText("Sensitivity:")
        self._sensitivity.SetBalloonHelpString("")

        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 2 -pady 2" % self._sensitivity.GetWidgetName())

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
        self._numberOfIterationsTag = self._parentClass.AddObserverByNumber(self._numberOfIterations,vtkKWThumbWheel_ValueChangedEvent)
        self._numberOfDiffusionSubIterationsTag = self._parentClass.AddObserverByNumber(self._numberOfDiffusionSubIterations,vtkKWThumbWheel_ValueChangedEvent)
        self._sigmaMinTag = self._parentClass.AddObserverByNumber(self._sigmaMin.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._sigmaMaxTag = self._parentClass.AddObserverByNumber(self._sigmaMax.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._alphaTag = self._parentClass.AddObserverByNumber(self._alpha.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._betaTag = self._parentClass.AddObserverByNumber(self._beta.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._gammaTag = self._parentClass.AddObserverByNumber(self._gamma.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._timestepTag = self._parentClass.AddObserverByNumber(self._timestep.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._epsilonTag = self._parentClass.AddObserverByNumber(self._epsilon.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._wstrengthTag = self._parentClass.AddObserverByNumber(self._wstrength.GetWidget(),vtkKWSpinBox_ValueChangedEvent)
        self._sensitivityTag = self._parentClass.AddObserverByNumber(self._sensitivity.GetWidget(),vtkKWSpinBox_ValueChangedEvent)



        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)



    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)

    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)

        if caller == self._numberOfSigmaSteps and event == vtkKWThumbWheel_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._numberOfIterations and event == vtkKWThumbWheel_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._numberOfDiffusionSubIterations and event == vtkKWThumbWheel_ValueChangedEvent:
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
        elif caller == self._timestep.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._epsilon.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._wstrength.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()
        elif caller == self._sensitivity.GetWidget() and event == vtkKWSpinBox_ValueChangedEvent:
            self._parentClass.UpdateMRML()

        elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            self.Execute()
            self._parentClass.UpdateMRML()


    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        if node:

            node.SetParameter('VEDM_numberOfSigmaSteps',self._numberOfSigmaSteps.GetValue())
            node.SetParameter('VEDM_numberOfIterations',self._numberOfIterations.GetValue())
            node.SetParameter('VEDM_numberOfDiffusionSubIterations',self._numberOfDiffusionSubIterations.GetValue())
            node.SetParameter('VEDM_sigmaMin',self._sigmaMin.GetWidget().GetValue())
            node.SetParameter('VEDM_sigmaMax',self._sigmaMax.GetWidget().GetValue())
            node.SetParameter('VEDM_alpha',self._alpha.GetWidget().GetValue())
            node.SetParameter('VEDM_beta',self._beta.GetWidget().GetValue())
            node.SetParameter('VEDM_gamma',self._gamma.GetWidget().GetValue())
            node.SetParameter('VEDM_timestep',self._timestep.GetWidget().GetValue())
            node.SetParameter('VEDM_epsilon',self._epsilon.GetWidget().GetValue())
            node.SetParameter('VEDM_wstrength',self._wstrength.GetWidget().GetValue())
            node.SetParameter('VEDM_sensitivity',self._sensitivity.GetWidget().GetValue())


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

            if node.GetParameter('VEDM_numberOfSigmaSteps'):
                self._numberOfSigmaSteps.SetValue(node.GetParameter('VEDM_numberOfSigmaSteps'))

            if node.GetParameter('VEDM_numberOfIterations'):
                self._numberOfIterations.SetValue(node.GetParameter('VEDM_numberOfIterations'))

            if node.GetParameter('VEDM_numberOfDiffusionSubIterations'):
                self._numberOfDiffusionSubIterations.SetValue(node.GetParameter('VEDM_numberOfDiffusionSubIterations'))

            if node.GetParameter('VEDM_sigmaMin'):
                self._sigmaMin.GetWidget().SetValue(node.GetParameter('VEDM_sigmaMin'))

            if node.GetParameter('VEDM_sigmaMax'):
                self._sigmaMax.GetWidget().SetValue(node.GetParameter('VEDM_sigmaMax'))

            if node.GetParameter('VEDM_alpha'):
                self._alpha.GetWidget().SetValue(node.GetParameter('VEDM_alpha'))

            if node.GetParameter('VEDM_beta'):
                self._beta.GetWidget().SetValue(node.GetParameter('VEDM_beta'))

            if node.GetParameter('VEDM_gamma'):
                self._gamma.GetWidget().SetValue(node.GetParameter('VEDM_gamma'))

            if node.GetParameter('VEDM_timestep'):
                self._timestep.GetWidget().SetValue(node.GetParameter('VEDM_timestep'))

            if node.GetParameter('VEDM_epsilon'):
                self._epsilon.GetWidget().SetValue(node.GetParameter('VEDM_epsilon'))

            if node.GetParameter('VEDM_wstrength'):
                self._wstrength.GetWidget().SetValue(node.GetParameter('VEDM_wstrength'))

            if node.GetParameter('VEDM_sensitivity'):
                self._sensitivity.GetWidget().SetValue(node.GetParameter('VEDM_sensitivity'))

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
            slicer.Application.ErrorMessage("No input volume or no output volume found. Aborting VEDM..\n")
            return
        else:

            sigmaMin = float(self._sigmaMin.GetWidget().GetValue())
            sigmaMax = float(self._sigmaMax.GetWidget().GetValue())
            numberOfSigmaSteps =  int(self._numberOfSigmaSteps.GetValue())
            numberOfIterations =  int(self._numberOfIterations.GetValue())
            numberOfDiffusionSubIterations =  int(self._numberOfDiffusionSubIterations.GetValue())
            alpha = float(self._alpha.GetWidget().GetValue())
            beta = float(self._beta.GetWidget().GetValue())
            gamma = float(self._gamma.GetWidget().GetValue())
            timestep = float(self._timestep.GetWidget().GetValue())
            epsilon = float(self._epsilon.GetWidget().GetValue())
            wstrength = float(self._wstrength.GetWidget().GetValue())
            sensitivity = float(self._sensitivity.GetWidget().GetValue())

            outVolumeImage = self._parentClass._logic.ApplyVEDM(inVolume.GetImageData(),sigmaMin,sigmaMax,numberOfSigmaSteps,alpha,beta,gamma,timestep,epsilon,wstrength,sensitivity,numberOfIterations,numberOfDiffusionSubIterations)

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
        self._numberOfIterations.SetValue(3)
        self._numberOfDiffusionSubIterations.SetValue(1)
        self._sigmaMin.GetWidget().SetValue(1)
        self._sigmaMax.GetWidget().SetValue(5)
        self._alpha.GetWidget().SetValue(0.5)
        self._beta.GetWidget().SetValue(0.5)
        self._gamma.GetWidget().SetValue(5.0)
        self._timestep.GetWidget().SetValue(1E-2)
        self._epsilon.GetWidget().SetValue(1E-2)
        self._wstrength.GetWidget().SetValue(25.0)
        self._sensitivity.GetWidget().SetValue(5.0)





