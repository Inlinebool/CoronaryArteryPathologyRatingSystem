from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton

from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000

###
### seeds initialization page (derived from skeleton)
###
class SlicerVMTKInitializationSeedsGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._seedFiducialList = None

        self._firstRowFrame = slicer.vtkKWFrame()
        self._seedPointsFrame = slicer.vtkKWFrameWithLabel()
        self._addSeedPointButton = slicer.vtkKWPushButton()
        self._delSeedPointButton = slicer.vtkKWPushButton()
        self._seedPointsList = slicer.vtkKWListBoxWithScrollbars()
        self._startButton = slicer.vtkKWPushButton()
        self._resetButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._seedFiducialList = None

        self._firstRowFrame.SetParent(None)
        self._firstRowFrame = None
        self._seedPointsFrame.SetParent(None)
        self._seedPointsFrame = None
        self._seedPointsList.SetParent(None)
        self._seedPointsList = None
        self._addSeedPointButton.SetParent(None)
        self._addSeedPointButton = None
        self._delSeedPointButton.SetParent(None)
        self._delSeedPointButton = None

        self._startButton.SetParent(None)
        self._startButton = None
        self._resetButton.SetParent(None)
        self._resetButton = None


    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        if self._seedFiducialList != None:
            node.SetParameter('SE_seedFiducialList',self._seedFiducialList.GetID())
        else:
            node.SetParameter('SE_seedFiducialList',"None")

    def UpdateGUI(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUI(self)

        node = self._parentClass.GetScriptedModuleNode()

        self._seedFiducialList = None

        if (node.GetParameter("SE_seedFiducialList")!="None" and node.GetParameter("SE_seedFiducialList")):
            self._seedFiducialList = self._parentClass.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter("SE_seedFiducialList"))

        self.UpdateGUIByState()


    # belongs to UpdateGUI
    def UpdateGUIByState(self):

        self._seedPointsFrame.AllowFrameToCollapseOff()
        self._seedPointsFrame.SetLabelText("Seeds")
        self._seedPointsFrame.SetReliefToSunken()

        self._addSeedPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addSeedPointButton.SetReliefToRaised()
        self._addSeedPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addSeedPointButton.SetForegroundColor(0.2,0.6,0.2)
        self._addSeedPointButton.SetText("Add Seed Point")
        self._addSeedPointButton.SetWidth(15)
        self._addSeedPointButton.SetBalloonHelpString("Click to add new seed point")

        self._delSeedPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._delSeedPointButton.SetReliefToRaised()
        self._delSeedPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._delSeedPointButton.SetForegroundColor(0.9,0.2,0.2)
        self._delSeedPointButton.SetText("X")
        self._delSeedPointButton.SetWidth(3)
        self._delSeedPointButton.SetBalloonHelpString("Click to delete selected seed point")

        self._seedPointsList.GetWidget().SetHeight(3)
        self._seedPointsList.GetWidget().SetSelectionModeToSingle()
        self._seedPointsList.GetWidget().DeleteAll()

        self._startButton.SetEnabled(0)
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

        if self._seedFiducialList != None:

            numberOfFiducials = self._seedFiducialList.GetNumberOfFiducials()

            if numberOfFiducials==0:

                self._seedPointsList.GetWidget().AppendUnique("<no seed points>")   

            else:

                for i in range(0,numberOfFiducials):

                    curLabelText = self._seedFiducialList.GetNthFiducialLabelText(i)
                    curCoords = self._seedFiducialList.GetNthFiducialXYZ(i)

                    self._seedPointsList.GetWidget().AppendUnique(curLabelText+" - R:" + str(round(curCoords[0],1)) + " A:" + str(round(curCoords[1],1)) + " S:" + str(round(curCoords[2],1)))

                # at least one fiducial exists
                self._startButton.SetEnabled(1)

        else:

            self._seedPointsList.GetWidget().AppendUnique("<no seed points>")

    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)

        self._firstRowFrame.SetParent(self._parentFrame)
        self._firstRowFrame.Create()

        self._seedPointsFrame.SetParent(self._parentFrame)
        self._seedPointsFrame.Create()

        self._addSeedPointButton.SetParent(self._seedPointsFrame.GetFrame())
        self._addSeedPointButton.Create()

        self._delSeedPointButton.SetParent(self._seedPointsFrame.GetFrame())
        self._delSeedPointButton.Create()

        self._seedPointsList.SetParent(self._seedPointsFrame.GetFrame())
        self._seedPointsList.Create()

        self._startButton.SetParent(self._parentFrame)
        self._startButton.Create()

        self._resetButton.SetParent(self._parentFrame)
        self._resetButton.Create()

        self.UpdateGUIByState()

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._firstRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))

        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._seedPointsFrame.GetWidgetName(), self._firstRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._addSeedPointButton.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._seedPointsList.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand n -padx 2 -pady 2" % (self._delSeedPointButton.GetWidgetName()))

        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._startButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._resetButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
    
    def AddGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.AddGUIObservers(self)

        self._addSeedPointButtonTag = self._parentClass.AddObserverByNumber(self._addSeedPointButton,vtkKWPushButton_InvokedEvent)
        self._delSeedPointButtonTag = self._parentClass.AddObserverByNumber(self._delSeedPointButton,vtkKWPushButton_InvokedEvent)

        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._resetButtonTag = self._parentClass.AddObserverByNumber(self._resetButton,vtkKWPushButton_InvokedEvent)


    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)


        self._parentClass.RemoveObserver(self._addSeedPointButtonTag)
        self._parentClass.RemoveObserver(self._delSeedPointButtonTag)
        self._parentClass.RemoveObserver(self._startButtonTag)
        self._parentClass.RemoveObserver(self._resetButtonTag)


    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)
        

        if caller == self._addSeedPointButton and event == vtkKWPushButton_InvokedEvent:
            
            if self._parentClass.GetHelper().GetIsInteractiveMode() == 0:

                self.InitAddSeedPoint()

            elif self._parentClass.GetHelper().GetIsInteractiveMode() == 1:

                self.TeardownAddSeedPoint()

                    

        elif caller == self._delSeedPointButton and event == vtkKWPushButton_InvokedEvent:

            self.RemoveSeedPoint()
            self._parentClass.UpdateMRML()
            self.UpdateGUIByState()

        elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            
            self.Execute()
            self._parentClass.UpdateMRML()
        elif caller == self._resetButton and event == vtkKWPushButton_InvokedEvent:
            self.DeleteFiducialListsFromScene(3)
            self.Reset()
            self._parentClass.UpdateMRML()



    def DeleteFiducialListsFromScene(self,which):
        SlicerVMTKAdvancedPageSkeleton.DeleteFiducialListsFromScene(self,which)
        

        node = self._parentClass.GetScriptedModuleNode()

        if node:

            scene = self._parentClass.GetLogic().GetMRMLScene()

            if self._seedFiducialList!=None:
                if scene.IsNodePresent(self._seedFiducialList):
                    # node is in scene, now delete
                    scene.RemoveNode(self._seedFiducialList)
                    self._seedFiducialList = None



    def InitAddSeedPoint(self):

        scene = self._parentClass.GetLogic().GetMRMLScene()

        if self._seedFiducialList == None:
            
            # no list created yet
            self._seedFiducialList = slicer.vtkMRMLFiducialListNode()
            self._seedFiducialList.SetName("VMTK Seed Points")
            self._seedFiducialList.SetScene(scene)
            self._seedFiducialList.SetColor(0.2,0.6,0.2)
            self._seedFiducialList.SetGlyphTypeFromString("Circle2D")
            self._seedFiducialList.SetLocked(1)
            scene.AddNode(self._seedFiducialList)
            self._seedPointsList.GetWidget().DeleteAll()

        #disable all other buttons
        self._parentClass.UnLockInitInterface(0)
        self._startButton.SetEnabled(0)

        #change the button appeareance
        self._addSeedPointButton.SetActiveBackgroundColor(0.2,0.6,0.2)
        self._addSeedPointButton.SetReliefToSunken()
        self._addSeedPointButton.SetBackgroundColor(0.2,0.6,0.2)
        self._addSeedPointButton.SetForegroundColor(0.2,0.2,0.2)
        self._addSeedPointButton.SetText("Stop adding!")
        self._addSeedPointButton.SetWidth(15)
        self._addSeedPointButton.SetBalloonHelpString("Click to stop adding new seed points")


        self._parentClass.GetHelper().SetIsInteractiveMode(1,self)

        
    def TeardownAddSeedPoint(self):
    
        self._parentClass.GetHelper().SetIsInteractiveMode(0,None)

        #re-change the button appeareance
        self._addSeedPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addSeedPointButton.SetReliefToRaised()
        self._addSeedPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addSeedPointButton.SetForegroundColor(0.2,0.6,0.2)
        self._addSeedPointButton.SetText("Add Seed Point")
        self._addSeedPointButton.SetWidth(15)
        self._addSeedPointButton.SetBalloonHelpString("Click to add new seed point")

        self.UpdateGUIByState()
        self._parentClass.UpdateMRML()

    def RemoveSeedPoint(self):

        curSelectionId = self._seedPointsList.GetWidget().GetSelectionIndex()

        if curSelectionId != -1:

            #at least one item selected, but which
            curSelection = self._seedPointsList.GetWidget().GetSelection()

            if curSelection != "<no source points>":

                self._seedFiducialList.RemoveFiducial(curSelectionId)


    #
    # x,y
    # which is the Name of the SliceWindow (Red,Yellow,Green)
    #
    def HandleClickInSliceWindowWithCoordinates(self, which, coordinates):
        SlicerVMTKAdvancedPageSkeleton.HandleClickInSliceWindowWithCoordinates(self, which, coordinates)

        coordinatesRAS = self._parentClass.GetHelper().ConvertCoordinates2RAS(which,coordinates)
        fiducial = self._seedFiducialList.AddFiducialWithXYZ(coordinatesRAS[0], coordinatesRAS[1], coordinatesRAS[2],0)

        numberOfFiducials = self._seedFiducialList.GetNumberOfFiducials()

        lastFiducial = 1

        # always use new Ids for the fiducial label
        if numberOfFiducials != 1:
            for i in range(0,numberOfFiducials-1):
                currentFiducialLabel = self._seedFiducialList.GetNthFiducialLabelText(i)
                currentFiducialLabel = currentFiducialLabel.split("P")[1]
                if int(currentFiducialLabel) >= lastFiducial:
                    lastFiducial = int(currentFiducialLabel)+1

        self._seedFiducialList.SetNthFiducialLabelText(fiducial, "SP"+str(lastFiducial))
        self._parentClass.GetHelper().debug("Fiducial Added! More to come!")






    #
    # Execute the algorithm
    #
    def Execute(self):

        self._parentClass.SetUpdatingOn()

        if self._parentClass._initImageCheckbox.GetSelectedState()==1:
            inVolumeNode = self._parentClass._inVolumeSelectorSnd.GetSelected()
        else:
            inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()
        sourceSeedsNode = self._seedFiducialList

        myLogic = self._parentClass.GetMyLogic()
        resultContainer = myLogic.ExecuteSeeds(inVolumeNode,sourceSeedsNode)
        resultContainer = self._parentClass.GetHelper().SetAndMergeInitVolume(resultContainer)
        self._parentClass.GetHelper().GenerateInitializationModel(resultContainer)

        self._parentClass.SetUpdatingOff()
        self._parentClass._state = 1
        self._parentClass.UpdateGUIByState()
        self._parentClass.UpdateMRML() # save the results


    #
    # Resets the GUI, all fiducial lists and sets any values to default
    #
    def Reset(self):
        SlicerVMTKAdvancedPageSkeleton.Reset(self)

        self._seedFiducialList = None

        self.UpdateGUIByState()

