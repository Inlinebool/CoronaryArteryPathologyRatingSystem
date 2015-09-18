from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer


from time import strftime

from SlicerVMTKVesselEnhancementFrangiGUI import SlicerVMTKVesselEnhancementFrangiGUI
from SlicerVMTKVesselEnhancementSatoGUI import SlicerVMTKVesselEnhancementSatoGUI
from SlicerVMTKVesselEnhancementVEDGUI import SlicerVMTKVesselEnhancementVEDGUI
from SlicerVMTKVesselEnhancementLogic import SlicerVMTKVesselEnhancementLogic


vtkKWPushButton_InvokedEvent = 10000

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000

class VMTKVesselEnhancement(ScriptedModuleGUI):

    def debug(self,msg):

        '''debug prints to stdout (better than print because of flush)'''

        # declaration of new variable without type specification
        debugMode = 0

        if debugMode: # debugMode is a bool

            # the print statement needs strings as input, so every value to output has to be
            # casted
            print "[slicerVMTKVesselEnhancement " + strftime("%H:%M:%S") + "] " + str(msg)
            import sys
            sys.stdout.flush()

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        self.SetModuleName("VMTKVesselEnhancement")
        self.SetGUIName("Vessel Enhancement using VMTK")

        self._moduleFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._moduleNodeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._moduleExistingSetsNodeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._inVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()

        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._advancedFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._advancedTabs = slicer.vtkKWNotebook()

        self._dummyLabel = slicer.vtkKWPushButton()

        self._logic = SlicerVMTKVesselEnhancementLogic(self)

        self._presetsScene = None # a new MRML Scene for the self._presetsScene environment


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

        self._advancedFrame.SetParent(None)
        self._advancedFrame = None
        self._advancedTabs.SetParent(None)
        self._advancedTabs = None

        self._logic = None

    def RemoveMRMLNodeObservers(self):
        pass
    
    def RemoveLogicObservers(self):
        pass

    def AddGUIObservers(self):
        self._moduleExistingSetsNodeSelectorSelectedTag = self.AddObserverByNumber(self._moduleExistingSetsNodeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._moduleNodeSelectorSelectedTag = self.AddObserverByNumber(self._moduleNodeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._inVolumeSelectorSelectedTag = self.AddObserverByNumber(self._inVolumeSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)

        for page in self._pages:
            page.AddGUIObservers()

    def RemoveGUIObservers(self):
        self._moduleExistingSetsNodeSelectorSelectedTag = None
        self.__moduleNodeSelectorSelectedTag = None
        self._inVolumeSelectorSelectedTag = None

        for page in self._pages:
            page.RemoveGUIObservers()

    def ProcessGUIEvents(self,caller,event):
        if not self._updating:

            if caller == self._inVolumeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._inVolumeSelector.GetSelected():
                self.UpdateMRML() # update reference to volume
                self.UpdateGUI()
            elif caller == self._outVolumeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._outVolumeSelector.GetSelected():
                self.UpdateMRML() # update reference to volume
            elif caller == self._moduleNodeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._moduleNodeSelector.GetSelected():
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetAndObserveScriptedModuleNode(node)

                self.UpdateGUI()
            elif caller == self._moduleExistingSetsNodeSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._moduleExistingSetsNodeSelector.GetSelected():
                self.UpdateGUIByPreset()
                self.UpdateMRML()

            for page in self._pages:
                page.ProcessGUIEvents(caller,event)


    def UpdateMRML(self):

        if not self._updating:

            self._updating = 1

            self.debug("calling UpdateMRML")

            node = self.GetScriptedModuleNode()

            if not node or not self._moduleNodeSelector.GetSelected():
                self.debug("no node associated to this scriptedmodule, creating new..")
                self._moduleNodeSelector.SetSelectedNew("vtkMRMLScriptedModuleNode")
                self._moduleNodeSelector.ProcessNewNodeCommand("vtkMRMLScriptedModuleNode", "EnhancementParameters")
                node = self._moduleNodeSelector.GetSelected()
                self.GetLogic().SetAndObserveScriptedModuleNode(node)
                self.SetScriptedModuleNode(node)
                self.debug("new node created!")



            for page in self._pages:
                page.UpdateMRML()

            node.SetParameter('isValidVMTKnode',"1")

            node.SetParameter('raisedPage', str(self._advancedTabs.GetRaisedPageId()))


            self.GetLogic().GetMRMLScene().SaveStateForUndo(node)


            node.RequestParameterList()
            self.debug("parameterlist which was just set in main UpdateMRML " + node.GetParameterList())

            self._updating = 0

    def UpdateGUI(self):

        if not self._updating:

            self._updating = 1


            node = self.GetScriptedModuleNode()

            self.debug("calling UpdateGUI")

            if node:

                if str(node.GetParameter('isValidVMTKnode'))=="1":

                    self.debug("found valid VMTK node")

                    for page in self._pages:
                        page.UpdateGUI()

                    if (node.GetParameter('raisedPage')):
                        self._advancedTabs.RaisePage(node.GetParameter('raisedPage'))

                    node.RequestParameterList()
                    self.debug("parameterlist which was just read in main UpdateGUI " + str(node.GetParameterList()))

                    self.CreateOutVolumeNode()
                
                else:

                    for page in self._pages:
                        page.Reset()

            self._updating = 0

    def UpdateGUIByPreset(self):

        node = self._moduleExistingSetsNodeSelector.GetSelected()

        if node:

            node.RequestParameterList()
            self.debug("parameterlist which was just read in main UpdateGUIByPreset " + str(node.GetParameterList()))

            if (node.GetParameter('raisedPage')!=""):
                self.debug("Raising page "+str(node.GetParameter('raisedPage')))
                self._advancedTabs.RaisePage(node.GetParameter('raisedPage'))

            for page in self._pages:
                page.UpdateGUIByPreset()

    def CreateOutVolumeNode(self):

        if not self._outVolumeSelector.GetSelected():

            self._outVolumeSelector.SetSelectedNew("vtkMRMLScalarVolumeNode")
            self._outVolumeSelector.ProcessNewNodeCommand("vtkMRMLScalarVolumeNode", "EnhancedVesselnessOut")


    def ProcessMRMLEvents(self,caller,event):
        pass

    def LoadPresets(self):

        scriptedModuleNode = slicer.vtkMRMLScriptedModuleNode()

        self._presetsScene = slicer.vtkMRMLScene()
        self._presetsScene.RegisterNodeClass(scriptedModuleNode)

        presetFileName = str(slicer.Application.GetExtensionsInstallPath())+"/"+str(slicer.Application.GetSvnRevision())+"/"+self.GetModuleName()+"/"+self.GetModuleName()+"/presets.xml";
        self.debug("presetFileName: " + presetFileName)

        self._presetsScene.SetURL(presetFileName)
        self._presetsScene.Connect()

        self._moduleExistingSetsNodeSelector.SetMRMLScene(self._presetsScene)

    def ProcessClickOnInitTabs(self):

        self.debug("processing tab click..")

        if self._updating != 1:

            self.UpdateMRML()

    def BuildGUI(self):

        self.GetUIPanel().AddPage("VesselEnhancement","VesselEnhancement","")
        self._vmtkVesEnhPage = self.GetUIPanel().GetPageWidget("VesselEnhancement")
        helpText = "**Vessel Enhancement using VMTK**, developed by Daniel Haehn.\n\nAttention: This module needs the VMTK libraries which are available inside the VmtkSlicerModule extension.\n\nDocumentation and Tutorials are available at: <a>http://wiki.slicer.org/slicerWiki/index.php/Modules:VMTKVesselEnhancement</a>\n\n**Instructions:**\nFrangi and Sato without Parameter Sets:\n1. Specify the Input Volume.\n2. Optional: Specify the Output Volume\n3. Choose the algorithm using the tabs.\n4. Specify the diameter size (in mm or voxels) to detect. The number of steps defines the detection accuracy between the minimal and maximal diameter size.\n5. Press Start and when finished (the stdout shows progress), the vessel enhanced volume appears within the slice viewers.\n\n\nParameter Sets for Sato Vesselness:\nParameter presets for certain Use Cases exist and set the minimal and maximal diameters automatically.\n\n\nFor further information on FrangiVesselness see <a>http://www.tecn.upf.es/~afrangi/articles/miccai1998.pdf</a>.\n\n\nDetails on SatoVesselness can be found here <a>http://www.spl.harvard.edu/archive/spl-pre2007/pages/papers/yoshi/cr.html</a>.\n\n\nInformation to Vessel Enhancement Diffusion is available at <a>http://www.springerlink.com/content/d11hxca163edccwk/fulltext.pdf</a>.\n\nPlease note that the GUI for Vessel Enhancement Diffusion is still Under Construction!"
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer Community. See http://www.slicer.org for details."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._vmtkVesEnhPage,helpText,aboutText)

        self.debug("Creating VesselEnhancement GUI")


        self._moduleFrame.SetParent(self._vmtkVesEnhPage)
        self._moduleFrame.Create()
        self._moduleFrame.SetLabelText("VMTKVesselEnhancement")
        self._moduleFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -expand y -padx 2 -pady 2 -in %s" % (self._moduleFrame.GetWidgetName(),self._vmtkVesEnhPage.GetWidgetName()))


        self._moduleExistingSetsNodeSelector.SetNodeClass("vtkMRMLScriptedModuleNode", "", "", "")
        self._moduleExistingSetsNodeSelector.NoneEnabledOn()
        self._moduleExistingSetsNodeSelector.ShowHiddenOn()
        self._moduleExistingSetsNodeSelector.SetParent(self._moduleFrame.GetFrame())
        self._moduleExistingSetsNodeSelector.Create()
        self._moduleExistingSetsNodeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._moduleExistingSetsNodeSelector.UpdateMenu()
        self._moduleExistingSetsNodeSelector.SetBorderWidth(2)
        self._moduleExistingSetsNodeSelector.SetLabelText("Existing Parameter Sets:")
        self._moduleExistingSetsNodeSelector.SetBalloonHelpString("select a VMTK Vessel Enhancement node with existing parameters.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._moduleExistingSetsNodeSelector.GetWidgetName())
    

        self._moduleNodeSelector.SetNodeClass("vtkMRMLScriptedModuleNode", "VMTKVesselEnhancement", self.GetLogic().GetModuleName(), "EnhancementParameters")
        self._moduleNodeSelector.NewNodeEnabledOn()
        self._moduleNodeSelector.NoneEnabledOn()
        self._moduleNodeSelector.ShowHiddenOn()
        self._moduleNodeSelector.SetParent(self._moduleFrame.GetFrame())
        self._moduleNodeSelector.Create()
        self._moduleNodeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._moduleNodeSelector.UpdateMenu()
        self._moduleNodeSelector.SetBorderWidth(2)
        self._moduleNodeSelector.SetLabelText("Module Parameters:")
        self._moduleNodeSelector.SetBalloonHelpString("select a VMTK Vessel Enhancement node from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 20 -pady 4" % self._moduleNodeSelector.GetWidgetName())


        self._topFrame.SetParent(self._moduleFrame.GetFrame())
        self._topFrame.Create()
        self._topFrame.SetLabelText("Input/Output")
        self._topFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -expand y -padx 2 -pady 2" % self._topFrame.GetWidgetName())


        self._inVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","","")
        self._inVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._inVolumeSelector.Create()
        self._inVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._inVolumeSelector.UpdateMenu()
        self._inVolumeSelector.SetBorderWidth(2)
        self._inVolumeSelector.SetLabelText("Input Volume: ")
        self._inVolumeSelector.SetBalloonHelpString("select an input volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 20 -pady 4" % self._inVolumeSelector.GetWidgetName())


        self._outVolumeSelector.SetNodeClass("vtkMRMLScalarVolumeNode","","","EnhancedVesselnessOut")
        self._outVolumeSelector.SetNewNodeEnabled(1)
        self._outVolumeSelector.SetParent(self._topFrame.GetFrame())
        self._outVolumeSelector.Create()
        self._outVolumeSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outVolumeSelector.UpdateMenu()
        self._outVolumeSelector.SetBorderWidth(2)
        self._outVolumeSelector.SetLabelText("Output Volume: ")
        self._outVolumeSelector.SetBalloonHelpString("select an output volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 20 -pady 4" % self._outVolumeSelector.GetWidgetName())

        # initialization tabs start here
        self._advancedFrame.SetParent(self._moduleFrame.GetFrame())
        self._advancedFrame.Create()
        self._advancedFrame.SetLabelText("Vessel Enhancement")
        self._advancedFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -expand y -fill x -padx 2 -pady 2" % self._advancedFrame.GetWidgetName())


        self._advancedTabs.SetParent(self._advancedFrame.GetFrame())
        self._advancedTabs.Create()
        self._advancedTabs.AddObserver(2089,self.ProcessClickOnInitTabs)

        slicer.TkCall("pack %s -side top -anchor nw -expand y -fill both -padx 2 -pady 2" % self._advancedTabs.GetWidgetName())

        self._advancedTabs.AddPage("FrangiVesselness","FrangiVesselness","")
        id = self._advancedTabs.GetFrame("FrangiVesselness")
        self._advancedFrangiPanel = SlicerVMTKVesselEnhancementFrangiGUI(id,self)
        self._advancedFrangiPanel.BuildGUI()
        self._pages.append(self._advancedFrangiPanel)
        #slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedTabs.GetWidgetName())

        self._advancedTabs.AddPage("SatoVesselness","SatoVesselness","")
        #slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._advancedTabs.GetWidgetName())
        id = self._advancedTabs.GetFrame("SatoVesselness")
        self._advancedSatoPanel = SlicerVMTKVesselEnhancementSatoGUI(id,self)
        self._advancedSatoPanel.BuildGUI()
        self._pages.append(self._advancedSatoPanel)

        self._advancedTabs.AddPage("VED","VesselEnhancingDiffusion (interface under construction)","")
        id = self._advancedTabs.GetFrame("VED")
        self._advancedVEDPanel = SlicerVMTKVesselEnhancementVEDGUI(id,self)
        self._advancedVEDPanel.BuildGUI()
        self._pages.append(self._advancedVEDPanel)


        self._dummyLabel.SetParent(self._moduleFrame.GetFrame())
        self._dummyLabel.Create()
        self._dummyLabel.SetText("")
        self._dummyLabel.SetWidth(1)
        self._dummyLabel.SetReliefToFlat()
        slicer.TkCall("pack %s -side top -anchor e -expand y -padx 1 -pady 1" % self._dummyLabel.GetWidgetName())

        self._advancedTabs.RaisePage(1)


        self.LoadPresets()



    def TearDownGUI(self):
        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("VesselEnhancement")

            
