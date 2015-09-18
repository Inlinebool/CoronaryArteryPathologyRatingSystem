from SlicerScriptedModule import ScriptedModuleGUI
from Slicer import slicer

from VMTKCenterlinesHelper import VMTKCenterlinesHelper
from VMTKCenterlinesLogic import VMTKCenterlinesLogic

vtkKWPushButton_InvokedEvent = 10000

vtkMRMLScene_CloseEvent = 66003

vtkSlicerNodeSelectorWidget_NodeSelectedEvent = 11000

class VMTKCenterlinesGUI(ScriptedModuleGUI):

    def __init__(self):

        ScriptedModuleGUI.__init__(self)

        self.SetCategory("Vascular Modeling Toolkit")
        self.SetGUIName("Centerline computation using VMTK")

        self._moduleFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._inModelSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._seedsSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._targetSeedsSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outModelPrepSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outModelSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._fiducialSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._importModelSelector = slicer.vtkSlicerNodeSelectorWidget()
        self._outVSelector = slicer.vtkSlicerNodeSelectorWidget()



        self._topFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._sndFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._sndFrameb = slicer.vtkSlicerModuleCollapsibleFrame()
        self._thirdFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._fourthFrame = slicer.vtkSlicerModuleCollapsibleFrame()
        self._fifthFrame = slicer.vtkSlicerModuleCollapsibleFrame()

        self._startButton = slicer.vtkKWPushButton()

        self._prepButton = slicer.vtkKWPushButton()

        self._saveButton = slicer.vtkKWLoadSaveButton()

        self._fidDensity = slicer.vtkKWSpinBoxWithLabel()
        self._fidButton = slicer.vtkKWPushButton()

    	self._exportDetails = slicer.vtkKWCheckButton()
    	self._exportHeaders = slicer.vtkKWCheckButton()
    	self._exportNifti = slicer.vtkKWCheckButton()

        self._exportButton = slicer.vtkKWPushButton()

        self._loadButton = slicer.vtkKWLoadSaveButton()

    	self._importHeaders = slicer.vtkKWCheckButton()
    	self._importNifti = slicer.vtkKWCheckButton()


        self._importButton = slicer.vtkKWPushButton()

        self._helper = VMTKCenterlinesHelper(self)

        self._logic = VMTKCenterlinesLogic(self)

        self._updating = 0

    def Destructor(self):



        self._helper = None
        self._logic = None

    def RemoveMRMLNodeObservers(self):
        pass
    
    def RemoveLogicObservers(self):
        pass

    def AddGUIObservers(self):

        self._seedsSelectorSelectedTag = self.AddObserverByNumber(self._seedsSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)
        self._targetSeedsSelectorSelectedTag = self.AddObserverByNumber(self._targetSeedsSelector,vtkSlicerNodeSelectorWidget_NodeSelectedEvent)

        self._startButtonTag = self.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)
        self._prepButtonTag = self.AddObserverByNumber(self._prepButton,vtkKWPushButton_InvokedEvent)
        self._fidButtonTag = self.AddObserverByNumber(self._fidButton,vtkKWPushButton_InvokedEvent)
        self._exportButtonTag = self.AddObserverByNumber(self._exportButton,vtkKWPushButton_InvokedEvent)
        self._importButtonTag = self.AddObserverByNumber(self._importButton,vtkKWPushButton_InvokedEvent)


    def RemoveGUIObservers(self):
        pass

    def ProcessGUIEvents(self,caller,event):
        if not self._updating:

            if caller == self._seedsSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._seedsSelector.GetSelected():
                self.SetActiveFiducialList(self._seedsSelector.GetSelected())
                self.UpdateMRML()
            elif caller == self._targetSeedsSelector and event == vtkSlicerNodeSelectorWidget_NodeSelectedEvent and self._targetSeedsSelector.GetSelected():
                self.SetActiveFiducialList(self._targetSeedsSelector.GetSelected())
                self.UpdateMRML()
            elif caller == self._prepButton and event == vtkKWPushButton_InvokedEvent:
                self.PrepCenterlines()
            elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
                self.Centerlines()
            elif caller == self._fidButton and event == vtkKWPushButton_InvokedEvent:
                self.Convert()
            elif caller == self._exportButton and event == vtkKWPushButton_InvokedEvent:
                self.Export()
            elif caller == self._importButton and event == vtkKWPushButton_InvokedEvent:
                self.Import()

            
    def PrepCenterlines(self):
        inModel = self._inModelSelector.GetSelected()
        outModel = self._outModelPrepSelector.GetSelected()


        vmtkFound = self.CheckForVmtkLibrary()

        if inModel and outModel and vmtkFound:

            displayNodeIn = inModel.GetModelDisplayNode()
            if displayNodeIn:
                displayNodeIn.SetVisibility(0)

            result = slicer.vtkPolyData()
            result.DeepCopy(self._logic.prepareModel(inModel.GetPolyData()))
            result.Update()
            outModel.SetAndObservePolyData(result)
            outModel.SetModifiedSinceRead(1)
            displayNode = outModel.GetModelDisplayNode()
            if not displayNode:
                displayNode = slicer.vtkMRMLModelDisplayNode()
            displayNode.SetPolyData(outModel.GetPolyData())
            displayNode.SetColor(0, 0.8, 0)
            displayNode.SetVisibility(1)
            displayNode.SetOpacity(0.7)
            self.GetLogic().GetMRMLScene().AddNode(displayNode)

            outModel.SetAndObserveDisplayNodeID(displayNode.GetID())

    def Centerlines(self):
        inModel = self._outModelPrepSelector.GetSelected()
        outModel = self._outModelSelector.GetSelected()
        vModel = self._outVSelector.GetSelected()

        seeds = self._seedsSelector.GetSelected()
        targetSeeds = self._targetSeedsSelector.GetSelected()

        vmtkFound = self.CheckForVmtkLibrary()

        if inModel and outModel and seeds and targetSeeds and vModel and vmtkFound:

            sourceSeedIds = slicer.vtkIdList()
            targetSeedIds = slicer.vtkIdList()

            pointLocator = slicer.vtkPointLocator()
            pointLocator.SetDataSet(inModel.GetPolyData())
            pointLocator.BuildLocator()

            for i in range(seeds.GetNumberOfFiducials()):
                rasPt = seeds.GetNthFiducialXYZ(i)
                id = pointLocator.FindClosestPoint(int(rasPt[0]),int(rasPt[1]),int(rasPt[2]))
                sourceSeedIds.InsertNextId(id)

            for i in range(targetSeeds.GetNumberOfFiducials()):
                rasPt = targetSeeds.GetNthFiducialXYZ(i)
                id = pointLocator.FindClosestPoint(int(rasPt[0]),int(rasPt[1]),int(rasPt[2]))
                targetSeedIds.InsertNextId(id)

            result = slicer.vtkPolyData()
            result.DeepCopy(self._logic.computeCenterlines(inModel.GetPolyData(),sourceSeedIds,targetSeedIds))
            result.Update()
            outModel.SetAndObservePolyData(result)
            outModel.SetModifiedSinceRead(1)
            displayNode = outModel.GetModelDisplayNode()
            if not displayNode:
                displayNode = slicer.vtkMRMLModelDisplayNode()
            displayNode.SetPolyData(outModel.GetPolyData())
            displayNode.SetColor(0, 0, 0)
            displayNode.SetVisibility(1)
            displayNode.SetOpacity(1.0)
            self.GetLogic().GetMRMLScene().AddNode(displayNode)

            outModel.SetAndObserveDisplayNodeID(displayNode.GetID())

            vd = slicer.vtkPolyData()
            vd.DeepCopy(self._logic.GetVoronoiDiagram())
            vd.Update()
            vModel.SetAndObservePolyData(vd)
            vModel.SetModifiedSinceRead(1)
            dNode = vModel.GetModelDisplayNode()
            if not dNode:
                dNode = slicer.vtkMRMLModelDisplayNode()
            dNode.SetPolyData(vModel.GetPolyData())
            dNode.SetScalarVisibility(1)
            dNode.SetBackfaceCulling(0)
            dNode.SetActiveScalarName("MaximumInscribedSphereRadius")
            dNode.SetAndObserveColorNodeID(self.GetLogic().GetMRMLScene().GetNodesByName("Labels").GetItemAsObject(0).GetID())
            dNode.SetVisibility(1)
            dNode.SetOpacity(0.5)
            self.GetLogic().GetMRMLScene().AddNode(dNode)

            vModel.SetAndObserveDisplayNodeID(dNode.GetID())

    def Export(self):
        outModel = self._outModelSelector.GetSelected()
        outputFileName = self._saveButton.GetFileName()


        if outModel and outputFileName:


            polyData = outModel.GetPolyData()

            f=open(outputFileName, 'w')
            line = "X Y Z"
            arrayNames = []
            dataArrays = polyData.GetPointData()

            if self._exportDetails.GetSelectedState()==1:
                for i in range(dataArrays.GetNumberOfArrays()):
                    array = dataArrays.GetArray(i)
                    arrayName = array.GetName()
                    if arrayName == None:
                        continue
                    if (arrayName[-1]=='_'):
                        continue
                    arrayNames.append(arrayName)
                    if (array.GetNumberOfComponents() == 1):
                        line = line + ' ' + arrayName
                    else:
                        for j in range(array.GetNumberOfComponents()):
                            line = line + ' ' + arrayName + str(j)
            line = line + '\n'
            if self._exportHeaders.GetSelectedState() == 1:
                f.write(line)
            numberOfLines = polyData.GetNumberOfPoints()

            for i in range(numberOfLines):
                point = polyData.GetPoint(numberOfLines - i - 1)
                if self._exportNifti.GetSelectedState()==1:
                    line = str(-1*point[0]) + ' ' + str(-1*point[1]) + ' ' + str(point[2])
                else:
                    line = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
                if self._exportDetails.GetSelectedState()==1:
                    for arrayName in arrayNames:
                        array = dataArrays.GetArray(arrayName)
                        for j in range(array.GetNumberOfComponents()):
                            line = line + ' ' + str(array.GetComponent(numberOfLines - i,j))
                line = line + '\n'
                f.write(line)

    def Convert(self):
        outFidList = self._fiducialSelector.GetSelected()
        density = self._fidDensity.GetWidget().GetValue()
        outModel = self._outModelSelector.GetSelected()

        if outFidList and density and outModel:

            polyData = outModel.GetPolyData()
            dcount = 0

            num = polyData.GetNumberOfPoints()

            for i in range(num):

                dcount = dcount + 1

                if dcount >= density:
                    dcount = 0
                    p = polyData.GetPoint(num - i - 1)
                    outFidList.AddFiducialWithXYZ(p[0], p[1], p[2], 0)



    def Import(self):
        outModel = self._importModelSelector.GetSelected()
        outputFileName = self._loadButton.GetFileName()

        if outModel and outputFileName:

            self._helper.debug("Start import..")

            points = slicer.vtkPoints()
            conn = slicer.vtkCellArray()
            polyData = slicer.vtkPolyData()

            f=open(outputFileName)
            lines = f.readlines()
            i = 0
            lastId = None
            for line in lines:

                if self._importHeaders.GetSelectedState()==1 and i==0:
                    self._helper.debug("Ignore first line..")
                else:
                    # now parse the rest
                    splitted = line.split()

                    x = float(splitted[0])
                    y = float(splitted[1])
                    z = float(splitted[2])

                    if self._importNifti.GetSelectedState()==1:
                        x = x*(-1)
                        y = y*(-1)

                    #self._helper.debug("Found point: "+str(x)+","+str(y)+","+str(z))

                    id = points.InsertNextPoint(x,y,z)
                    #self._helper.debug(id)

                    if lastId:
                        curLine = slicer.vtkLine()
                        curLine.GetPointIds().SetId(0,lastId)
                        curLine.GetPointIds().SetId(1,id)

                        conn.InsertNextCell(curLine)
                        #conn.InsertCellPoint(id)

                    lastId = id

                i = i+1

            f.close()

            result = slicer.vtkPolyData()
            result.SetPoints(points)
            result.SetLines(conn)
            result.Update()

            self._helper.debug(result)
            outModel.SetAndObservePolyData(result)
            outModel.SetModifiedSinceRead(1)
            displayNode = outModel.GetModelDisplayNode()
            if not displayNode:
                displayNode = slicer.vtkMRMLModelDisplayNode()
            displayNode.SetPolyData(outModel.GetPolyData())
            displayNode.SetColor(0.8, 0, 0)
            displayNode.SetVisibility(1)
            displayNode.SetOpacity(1.0)
            self.GetLogic().GetMRMLScene().AddNode(displayNode)

            outModel.SetAndObserveDisplayNodeID(displayNode.GetID())

    def SetActiveFiducialList(self,fiducialListNode):
        selectionNode = self.GetLogic().GetApplicationLogic().GetSelectionNode()
        selectionNode.SetReferenceActiveFiducialListID(fiducialListNode.GetID())

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

    def CreateOutModelNodes(self):

        if not self._outModelPrepSelector.GetSelected() or self._outModelPrepSelector.GetSelected()==self._inModelSelector.GetSelected():

            self._outModelPrepSelector.SetSelectedNew("vtkMRMLModelNode")
            self._outModelPrepSelector.ProcessNewNodeCommand("vtkMRMLModelNode", "VMTKCenterlinesPrepOut")

        if not self._outModelSelector.GetSelected() or self._outModelSelector.GetSelected()==self._inModelSelector.GetSelected():

            self._outModelSelector.SetSelectedNew("vtkMRMLModelNode")
            self._outModelSelector.ProcessNewNodeCommand("vtkMRMLModelNode", "VMTKCenterlinesOut")

        if not self._outVSelector.GetSelected() or self._outVSelector.GetSelected()==self._inModelSelector.GetSelected():

            self._outVSelector.SetSelectedNew("vtkMRMLModelNode")
            self._outVSelector.ProcessNewNodeCommand("vtkMRMLModelNode", "VMTKVoronoiOut")

        if not self._importModelSelector.GetSelected() or self._importModelSelector.GetSelected()==self._inModelSelector.GetSelected():

            self._importModelSelector.SetSelectedNew("vtkMRMLModelNode")
            self._importModelSelector.ProcessNewNodeCommand("vtkMRMLModelNode", "VMTKCenterlinesImport")


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

        self.GetUIPanel().AddPage("Centerlines","Centerlines","")
        self._centerlinePage = self.GetUIPanel().GetPageWidget("Centerlines")
        helpText = "**Centerline computation using VMTK**, developed by Daniel Haehn.\n\nAttention: This module needs the VMTK libraries which are available inside the VmtkSlicerModule extension.\n\nDocumentation and Tutorials are available at: <a>http://wiki.slicer.org/slicerWiki/index.php/Modules:VMTKCenterlines</a>\n\n**Instructions**\n1. Select the input model.\n2. Now prepare the model. Create a new output model node and click 'Prepare'. The model turns green.\n3. Place fiducials for the source and target points of the centerlines in the 3D window. One source and several target seeds are possible. The placement does not have to be exact. Create new output models for the Centerline and the Voronoi diagram. Click 'Get Centerlines!'.\n\n\nThe extracted centerlines can be exported using the export panel. Export details includes the maximum inscribed sphere radius (a.k.a. the vessel width for each centerline point)."
        aboutText = "This work is supported by NA-MIC, NAC, BIRN, NCIGT, and the Slicer Community. See http://www.slicer.org for details."
        self._helpAboutFrame = self.BuildHelpAndAboutFrame(self._centerlinePage,helpText,aboutText)

        self._helper.debug("Creating Centerlines GUI")

        self._moduleFrame.SetParent(self._centerlinePage)
        self._moduleFrame.Create()
        self._moduleFrame.SetLabelText("VMTKCenterlines")
        self._moduleFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._moduleFrame.GetWidgetName(),self._centerlinePage.GetWidgetName()))

        self._topFrame.SetParent(self._moduleFrame.GetFrame())
        self._topFrame.Create()
        self._topFrame.SetLabelText("Input")
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

        self._sndFrame.SetParent(self._moduleFrame.GetFrame())
        self._sndFrame.Create()
        self._sndFrame.SetLabelText("1. Preparation Step")
        self._sndFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._sndFrame.GetWidgetName())

        self._outModelPrepSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKCenterlinesPrepOut")
        self._outModelPrepSelector.SetNewNodeEnabled(1)
        self._outModelPrepSelector.SetParent(self._sndFrame.GetFrame())
        self._outModelPrepSelector.Create()
        self._outModelPrepSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outModelPrepSelector.UpdateMenu()
        self._outModelPrepSelector.SetBorderWidth(2)
        self._outModelPrepSelector.SetLabelText("Preparation Step Output Model: ")
        self._outModelPrepSelector.SetBalloonHelpString("select an output volume from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outModelPrepSelector.GetWidgetName())

        self._prepButton.SetParent(self._sndFrame.GetFrame())
        self._prepButton.Create()
        self._prepButton.SetEnabled(1)
        self._prepButton.SetText("Prepare Model!")
        self._prepButton.SetBalloonHelpString("Click to start the model preparation")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._prepButton.GetWidgetName())

        self._thirdFrame.SetParent(self._moduleFrame.GetFrame())
        self._thirdFrame.Create()
        self._thirdFrame.SetLabelText("2. Centerlines Computation")
        self._thirdFrame.ExpandFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._thirdFrame.GetWidgetName())


        self._seedsSelector.SetNodeClass("vtkMRMLFiducialListNode","","","Seeds")
        self._seedsSelector.SetParent(self._thirdFrame.GetFrame())
        self._seedsSelector.Create()
        self._seedsSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._seedsSelector.UpdateMenu()
        self._seedsSelector.SetNewNodeEnabled(1)
        self._seedsSelector.SetBorderWidth(2)
        self._seedsSelector.SetLabelText("Source Seeds: ")
        self._seedsSelector.SetBalloonHelpString("select a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._seedsSelector.GetWidgetName())

        self._targetSeedsSelector.SetNodeClass("vtkMRMLFiducialListNode","","","Targets")
        self._targetSeedsSelector.SetParent(self._thirdFrame.GetFrame())
        self._targetSeedsSelector.Create()
        self._targetSeedsSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._targetSeedsSelector.UpdateMenu()
        self._targetSeedsSelector.SetNewNodeEnabled(1)
        self._targetSeedsSelector.SetBorderWidth(2)
        self._targetSeedsSelector.SetLabelText("Target Seeds: ")
        self._targetSeedsSelector.SetBalloonHelpString("select a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._targetSeedsSelector.GetWidgetName())


        self._outModelSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKCenterlinesOut")
        self._outModelSelector.SetNewNodeEnabled(1)
        self._outModelSelector.SetParent(self._thirdFrame.GetFrame())
        self._outModelSelector.Create()
        self._outModelSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outModelSelector.UpdateMenu()
        self._outModelSelector.SetBorderWidth(2)
        self._outModelSelector.SetLabelText("Centerlines Output Model: ")
        self._outModelSelector.SetBalloonHelpString("select an output model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outModelSelector.GetWidgetName())

        self._outVSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKVoronoiOut")
        self._outVSelector.SetNewNodeEnabled(1)
        self._outVSelector.SetParent(self._thirdFrame.GetFrame())
        self._outVSelector.Create()
        self._outVSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._outVSelector.UpdateMenu()
        self._outVSelector.SetBorderWidth(2)
        self._outVSelector.SetLabelText("Voronoi Diagram: ")
        self._outVSelector.SetBalloonHelpString("select an output model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._outVSelector.GetWidgetName())


        self._startButton.SetParent(self._thirdFrame.GetFrame())
        self._startButton.Create()
        self._startButton.SetEnabled(1)
        self._startButton.SetText("Get Centerlines!")
        self._startButton.SetBalloonHelpString("Click to start the centerline computation")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._startButton.GetWidgetName())

        self._sndFrameb.SetParent(self._moduleFrame.GetFrame())
        self._sndFrameb.Create()
        self._sndFrameb.SetLabelText("3. Convert to Fiducial List")
        self._sndFrameb.CollapseFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._sndFrameb.GetWidgetName())

        self._fiducialSelector.SetNodeClass("vtkMRMLFiducialListNode","","","Centerlines")
        self._fiducialSelector.SetParent(self._sndFrameb.GetFrame())
        self._fiducialSelector.Create()
        self._fiducialSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._fiducialSelector.UpdateMenu()
        self._fiducialSelector.SetNewNodeEnabled(1)
        self._fiducialSelector.SetBorderWidth(2)
        self._fiducialSelector.SetLabelText("Output Fiducial List: ")
        self._fiducialSelector.SetBalloonHelpString("select a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._fiducialSelector.GetWidgetName())

        self._fidDensity.SetParent(self._sndFrameb.GetFrame())
        self._fidDensity.Create()
        self._fidDensity.GetWidget().SetRange(1,1000)
        self._fidDensity.GetWidget().SetIncrement(10)
        self._fidDensity.GetWidget().SetRestrictValueToInteger()
        self._fidDensity.GetWidget().SetValue(50)
        self._fidDensity.GetWidget().SetWidth(5)
        self._fidDensity.SetLabelText("Points between each fiducial placement:")
        self._fidDensity.SetBalloonHelpString("place fiducials every number of points entered")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 2" % self._fidDensity.GetWidgetName())

        self._fidButton.SetParent(self._sndFrameb.GetFrame())
        self._fidButton.Create()
        self._fidButton.SetText("Convert")
        self._fidButton.SetBalloonHelpString("Click to convert the centerline to a fiducial list")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._fidButton.GetWidgetName())
        
        
        self._fourthFrame.SetParent(self._moduleFrame.GetFrame())
        self._fourthFrame.Create()
        self._fourthFrame.SetLabelText("4. Export to file")
        self._fourthFrame.CollapseFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._fourthFrame.GetWidgetName())

        self._exportHeaders.SetParent(self._fourthFrame.GetFrame())
        self._exportHeaders.Create()
        self._exportHeaders.SetText("Add description headers")
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._exportHeaders.GetWidgetName())

        self._exportNifti.SetParent(self._fourthFrame.GetFrame())
        self._exportNifti.Create()
        self._exportNifti.SetText("Invert coordinates (IJK<->NIFTI)")
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._exportNifti.GetWidgetName())

        self._exportDetails.SetParent(self._fourthFrame.GetFrame())
        self._exportDetails.Create()
        self._exportDetails.SetText("Export details")
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._exportDetails.GetWidgetName())

        self._saveButton.SetParent(self._fourthFrame.GetFrame())
        self._saveButton.Create()
        self._saveButton.SetText("Select file..")
        self._saveButton.GetLoadSaveDialog().SaveDialogOn()
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._saveButton.GetWidgetName())

        self._exportButton.SetParent(self._fourthFrame.GetFrame())
        self._exportButton.Create()
        self._exportButton.SetEnabled(1)
        self._exportButton.SetText("Export!")
        self._exportButton.SetBalloonHelpString("Click to export")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._exportButton.GetWidgetName())


        self._fifthFrame.SetParent(self._moduleFrame.GetFrame())
        self._fifthFrame.Create()
        self._fifthFrame.SetLabelText("5. Import from file")
        self._fifthFrame.CollapseFrame()
        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2" % self._fifthFrame.GetWidgetName())

        self._loadButton.SetParent(self._fifthFrame.GetFrame())
        self._loadButton.Create()
        self._loadButton.SetText("Select file..")
        self._loadButton.GetLoadSaveDialog().SaveDialogOff()
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._loadButton.GetWidgetName())


        self._importHeaders.SetParent(self._fifthFrame.GetFrame())
        self._importHeaders.Create()
        self._importHeaders.SetText("Strip headers")
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._importHeaders.GetWidgetName())

        self._importNifti.SetParent(self._fifthFrame.GetFrame())
        self._importNifti.Create()
        self._importNifti.SetText("Invert coordinates (IJK<->NIFTI)")
        slicer.TkCall("pack %s -side top -anchor w -padx 2 -pady 2" % self._importNifti.GetWidgetName())


        self._importModelSelector.SetNodeClass("vtkMRMLModelNode","","1","VMTKCenterlinesImport")
        self._importModelSelector.SetNewNodeEnabled(1)
        self._importModelSelector.SetParent(self._fifthFrame.GetFrame())
        self._importModelSelector.Create()
        self._importModelSelector.SetMRMLScene(self.GetLogic().GetMRMLScene())
        self._importModelSelector.UpdateMenu()
        self._importModelSelector.SetBorderWidth(2)
        self._importModelSelector.SetLabelText("Imported Model Output: ")
        self._importModelSelector.SetBalloonHelpString("select an output model from the current mrml scene.")
        slicer.TkCall("pack %s -side top -anchor e -padx 20 -pady 4" % self._importModelSelector.GetWidgetName())

        self._importButton.SetParent(self._fifthFrame.GetFrame())
        self._importButton.Create()
        self._importButton.SetEnabled(1)
        self._importButton.SetText("Import!")
        self._importButton.SetBalloonHelpString("Click to import")
        slicer.TkCall("pack %s -side top -anchor e -padx 2 -pady 2" % self._importButton.GetWidgetName())


        #self.CreateOutModelNodes()

        self._helper.debug("Done Creating Centerlines GUI")


    def TearDownGUI(self):
        if self.GetUIPanel().GetUserInterfaceManager():
            self.GetUIPanel().RemovePage("Centerlines")

    def GetHelper(self):
        return self._helper

    def GetMyLogic(self):
        return self._logic

