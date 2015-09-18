from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000
vtkKWExtent_EndChangeEvent = 10002
vtkKWExtent_StartChangeEvent = 10000

###
### fast marching initialization page (derived from skeleton)
###
class SlicerVMTKInitializationFastMarchingGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._sourceFiducialList = None
        self._targetFiducialList = None

        self._currentFiducialList = None

        #top frame starts
        self._firstRowFrame = slicer.vtkKWFrame()

        # source frame starts
        self._sourcePointsFrame = slicer.vtkKWFrameWithLabel()

        self._addSourcePointButton = slicer.vtkKWPushButton()
        self._delSourcePointButton = slicer.vtkKWPushButton()
        self._sourcePointsList = slicer.vtkKWListBoxWithScrollbars()
   

        # target frame starts
        self._targetPointsFrame = slicer.vtkKWFrameWithLabel()

        self._addTargetPointButton = slicer.vtkKWPushButton()
        self._delTargetPointButton = slicer.vtkKWPushButton()
        self._targetPointsList = slicer.vtkKWListBoxWithScrollbars()

        #middle frame starts
        self._secondRowFrame = slicer.vtkKWFrame()

        #threshold frame starts
        self._thresholdFrame = slicer.vtkKWFrameWithLabel()
        self._thresholdSlider = slicer.vtkKWExtent()

        self._startButton = slicer.vtkKWPushButton()
        self._resetButton = slicer.vtkKWPushButton()


    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._sourceFiducialList = None
        self._targetFiducialList = None

        self._currentFiducialList = None

        self._firstRowFrame.SetParent(None)
        self._firstRowFrame = None
        self._sourcePointsFrame.SetParent(None)
        self._sourcePointsFrame = None
        self._sourcePointsList.SetParent(None)
        self._sourcePointsList = None

        self._targetPointsFrame.SetParent(None)
        self._targetPointsFrame = None

        self._targetPointsList.SetParent(None)
        self._targetPointsList = None

        self._addSourcePointButton.SetParent(None)
        self._addSourcePointButton = None

        self._addTargetPointButton.SetParent(None)
        self._addTargetPointButton = None

        self._delSourcePointButton.SetParent(None)
        self._delSourcePointButton = None

        self._delTargetPointButton.SetParent(None)
        self._delTargetPointButton = None

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


    def UpdateMRML(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateMRML(self)

        node = self._parentClass.GetScriptedModuleNode()

        if self._sourceFiducialList != None:
            node.SetParameter('FM_sourceFiducialList',self._sourceFiducialList.GetID())
        else:
            node.SetParameter('FM_sourceFiducialList',"None")

        if self._targetFiducialList != None:
            node.SetParameter('FM_targetFiducialList',self._targetFiducialList.GetID())
        else:
            node.SetParameter('FM_targetFiducialList',"None")

        extentValues = self._thresholdSlider.GetExtent()
        node.SetParameter('FM_lowerThreshold', extentValues[0])
        node.SetParameter('FM_higherThreshold', extentValues[1])

    def UpdateGUI(self):
        SlicerVMTKAdvancedPageSkeleton.UpdateGUI(self)

        node = self._parentClass.GetScriptedModuleNode()


        self._sourceFiducialList = None
        self._targetFiducialList = None

        self._currentFiducialList = None

        if (node.GetParameter("FM_sourceFiducialList")!="None" and node.GetParameter("FM_sourceFiducialList")):
            self._sourceFiducialList = self._parentClass.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter("FM_sourceFiducialList"))

        if (node.GetParameter("FM_targetFiducialList")!="None" and node.GetParameter("FM_targetFiducialList")):
            self._targetFiducialList = self._parentClass.GetLogic().GetMRMLScene().GetNodeByID(node.GetParameter("FM_targetFiducialList"))

        self.UpdateGUIByState()

        self._parentClass.SetUpdatingOn()
        self._thresholdSlider.SetExtent(node.GetParameter("FM_lowerThreshold"),node.GetParameter("FM_higherThreshold"),0,100,0,100)
        self._parentClass.SetUpdatingOff()

    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)

        self._firstRowFrame.SetParent(self._parentFrame)
        self._firstRowFrame.Create()

        self._sourcePointsFrame.SetParent(self._parentFrame)
        self._sourcePointsFrame.Create()

        self._addSourcePointButton.SetParent(self._sourcePointsFrame.GetFrame())
        self._addSourcePointButton.Create()

        self._delSourcePointButton.SetParent(self._sourcePointsFrame.GetFrame())
        self._delSourcePointButton.Create()

        self._sourcePointsList.SetParent(self._sourcePointsFrame.GetFrame())
        self._sourcePointsList.Create()
  
        self._targetPointsFrame.SetParent(self._parentFrame)
        self._targetPointsFrame.Create()

        self._addTargetPointButton.SetParent(self._targetPointsFrame.GetFrame())
        self._addTargetPointButton.Create()

        self._delTargetPointButton.SetParent(self._targetPointsFrame.GetFrame())
        self._delTargetPointButton.Create()

        self._targetPointsList.SetParent(self._targetPointsFrame.GetFrame())
        self._targetPointsList.Create()

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

        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._firstRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand y -padx 2 -pady 2 -in %s" % (self._secondRowFrame.GetWidgetName(), self._parentFrame.GetWidgetName()))

        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._sourcePointsFrame.GetWidgetName(), self._firstRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._addSourcePointButton.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._sourcePointsList.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand n -padx 2 -pady 2" % (self._delSourcePointButton.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._targetPointsFrame.GetWidgetName(), self._firstRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._addTargetPointButton.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._targetPointsList.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand n -padx 2 -pady 2" % (self._delTargetPointButton.GetWidgetName()))
        slicer.TkCall("pack %s -side left -expand y -padx 2 -pady 2 -in %s" % (self._thresholdFrame.GetWidgetName(), self._secondRowFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side top -expand n -padx 2 -pady 2" % (self._thresholdSlider.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._startButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
        slicer.TkCall("pack %s -side right -expand n -padx 2 -pady 2 -in %s" % (self._resetButton.GetWidgetName(), self._parentFrame.GetWidgetName()))
    
    # belongs to UpdateGUI
    def UpdateGUIByState(self):

        self._sourcePointsFrame.AllowFrameToCollapseOff()
        self._sourcePointsFrame.SetLabelText("Source points")
        self._sourcePointsFrame.SetReliefToSunken()

        self._addSourcePointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addSourcePointButton.SetReliefToRaised()
        self._addSourcePointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addSourcePointButton.SetForegroundColor(0.2,0.6,0.2)
        self._addSourcePointButton.SetText("Add Source Point")
        self._addSourcePointButton.SetWidth(15)
        self._addSourcePointButton.SetBalloonHelpString("Click to add new source point")

        self._delSourcePointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._delSourcePointButton.SetReliefToRaised()
        self._delSourcePointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._delSourcePointButton.SetForegroundColor(0.9,0.2,0.2)
        self._delSourcePointButton.SetText("X")
        self._delSourcePointButton.SetWidth(3)
        self._delSourcePointButton.SetBalloonHelpString("Click to delete selected source point")

        self._sourcePointsList.GetWidget().SetHeight(3)
        self._sourcePointsList.GetWidget().SetSelectionModeToSingle()
        self._sourcePointsList.GetWidget().DeleteAll()

        self._targetPointsFrame.AllowFrameToCollapseOff()
        self._targetPointsFrame.SetLabelText("Target points (optional)")
        self._targetPointsFrame.SetReliefToSunken()

        self._addTargetPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addTargetPointButton.SetReliefToRaised()
        self._addTargetPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addTargetPointButton.SetForegroundColor(0.2,0.2,0.6)
        self._addTargetPointButton.SetText("Add Target Point")
        self._addTargetPointButton.SetWidth(15)
        self._addTargetPointButton.SetBalloonHelpString("Click to add new target point")

        self._delTargetPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._delTargetPointButton.SetReliefToRaised()
        self._delTargetPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._delTargetPointButton.SetForegroundColor(0.9,0.2,0.2)
        self._delTargetPointButton.SetText("X")
        self._delTargetPointButton.SetWidth(3)
        self._delTargetPointButton.SetBalloonHelpString("Click to delete selected target point")

        self._targetPointsList.GetWidget().SetHeight(3)
        self._targetPointsList.GetWidget().SetSelectionModeToSingle()
        self._targetPointsList.GetWidget().DeleteAll()

        self._parentClass.SetUpdatingOn()
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
        self._thresholdSlider.SetEnabled(1)
        self._thresholdSlider.GetXRange().SetLabelText("Gray Values of Vessels")
        #self._thresholdSlider.SetEndCommand(self._parentClass.vtkScriptedModuleGUI, "Invoke CF_ExtentUpdate")
        self._parentClass.SetUpdatingOff()

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

        enoughInformation = False

        if self._sourceFiducialList != None:

            numberOfFiducials = self._sourceFiducialList.GetNumberOfFiducials()

            if numberOfFiducials==0:

                self._sourcePointsList.GetWidget().AppendUnique("<no source points>")   

            else:

                for i in range(0,numberOfFiducials):

                    curLabelText = self._sourceFiducialList.GetNthFiducialLabelText(i)
                    curCoords = self._sourceFiducialList.GetNthFiducialXYZ(i)

                    self._sourcePointsList.GetWidget().AppendUnique(curLabelText+" - R:" + str(round(curCoords[0],1)) + " A:" + str(round(curCoords[1],1)) + " S:" + str(round(curCoords[2],1)))

                    enoughInformation = True

        else:

            self._sourcePointsList.GetWidget().AppendUnique("<no source points>")


        if self._targetFiducialList != None:

            numberOfFiducials = self._targetFiducialList.GetNumberOfFiducials()

            if numberOfFiducials==0:

                self._targetPointsList.GetWidget().AppendUnique("<no target points>")   

            else:

                for i in range(0,numberOfFiducials):

                    curLabelText = self._targetFiducialList.GetNthFiducialLabelText(i)
                    curCoords = self._targetFiducialList.GetNthFiducialXYZ(i)

                    self._targetPointsList.GetWidget().AppendUnique(curLabelText+" - R:" + str(round(curCoords[0],1)) + " A:" + str(round(curCoords[1],1)) + " S:" + str(round(curCoords[2],1)))


        else:

            self._targetPointsList.GetWidget().AppendUnique("<no target points>")

        if enoughInformation: # target and source points exist
            self._startButton.SetEnabled(1)

    def AddGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.AddGUIObservers(self)

        self._addSourcePointButtonTag = self._parentClass.AddObserverByNumber(self._addSourcePointButton,vtkKWPushButton_InvokedEvent)
        self._delSourcePointButtonTag = self._parentClass.AddObserverByNumber(self._delSourcePointButton,vtkKWPushButton_InvokedEvent)
        self._addTargetPointButtonTag = self._parentClass.AddObserverByNumber(self._addTargetPointButton,vtkKWPushButton_InvokedEvent)
        self._delTargetPointButtonTag = self._parentClass.AddObserverByNumber(self._delTargetPointButton,vtkKWPushButton_InvokedEvent)

        self._thresholdSliderTag = self._parentClass.AddObserverByNumber(self._thresholdSlider, vtkKWExtent_EndChangeEvent)
        self._thresholdSliderRealtimeTag = self._parentClass.AddObserverByNumber(self._thresholdSlider, vtkKWExtent_StartChangeEvent)
        self._startButtonTag = self._parentClass.AddObserverByNumber(self._startButton,vtkKWPushButton_InvokedEvent)

        self._resetButtonTag = self._parentClass.AddObserverByNumber(self._resetButton,vtkKWPushButton_InvokedEvent)

    def RemoveGUIObservers(self):
        SlicerVMTKAdvancedPageSkeleton.RemoveGUIObservers(self)

        self._parentClass.RemoveObserver(self._addSourcePointButtonTag)
        self._parentClass.RemoveObserver(self._delSourcePointButtonTag)
        self._parentClass.RemoveObserver(self._addTargetPointButtonTag)
        self._parentClass.RemoveObserver(self._delTargetPointButtonTag)

        self._parentClass.RemoveObserver(self._thresholdSliderTag)

        self._parentClass.RemoveObserver(self._startButtonTag)
        self._parentClass.RemoveObserver(self._resetButtonTag)


    def ProcessGUIEvents(self,caller,event):
        SlicerVMTKAdvancedPageSkeleton.ProcessGUIEvents(self,caller,event)
        
        if caller == self._addSourcePointButton and event == vtkKWPushButton_InvokedEvent:
            if self._parentClass.GetHelper().GetIsInteractiveMode() == 0:
                self.InitAddSourcePoint()
            elif self._parentClass.GetHelper().GetIsInteractiveMode() == 1:
                self.TeardownAddSourcePoint()
        elif caller == self._delSourcePointButton and event == vtkKWPushButton_InvokedEvent:
            self.RemoveSourcePoint()
            self._parentClass.UpdateMRML()
            self.UpdateGUIByState()

        elif caller == self._addTargetPointButton and event == vtkKWPushButton_InvokedEvent:
            if self._parentClass.GetHelper().GetIsInteractiveMode() == 0:
                self.InitAddTargetPoint()
            elif self._parentClass.GetHelper().GetIsInteractiveMode() == 1:
                self.TeardownAddTargetPoint()
        elif caller == self._delTargetPointButton and event == vtkKWPushButton_InvokedEvent:
            self.RemoveTargetPoint()
            self._parentClass.UpdateMRML()
            self.UpdateGUIByState()

        elif caller == self._startButton and event == vtkKWPushButton_InvokedEvent:
            self.Execute()
            self._parentClass.UpdateMRML()
        elif caller == self._resetButton and event == vtkKWPushButton_InvokedEvent:
            self.DeleteFiducialListsFromScene(0)
            self.Reset()
            self._parentClass.UpdateMRML()
        elif caller == self._thresholdSlider and event == vtkKWExtent_StartChangeEvent:
            self._parentClass.Threshold(self._thresholdSlider.GetExtent())
        elif caller == self._thresholdSlider and event == vtkKWExtent_EndChangeEvent:
            self._parentClass.UpdateMRML()



    #
    # if which == 1, delete only source
    # if which == 2, delete only target
    # else delete both
    #
    def DeleteFiducialListsFromScene(self,which):
        SlicerVMTKAdvancedPageSkeleton.DeleteFiducialListsFromScene(self,which)
                
        node = self._parentClass.GetScriptedModuleNode()

        if node:

            scene = self._parentClass.GetLogic().GetMRMLScene()

            if (which!=2):

                if self._sourceFiducialList!=None:
                    if scene.IsNodePresent(self._sourceFiducialList):
                        # node is in scene, now delete
                        scene.RemoveNode(self._sourceFiducialList)
                        self._sourceFiducialList = None

            if (which!=1):

                if self._targetFiducialList!=None:
                    if scene.IsNodePresent(self._targetFiducialList):
                        # node is in scene, now delete
                        scene.RemoveNode(self._targetFiducialList)
                        self._targetFiducialList = None





    def InitAddSourcePoint(self):

        scene = self._parentClass.GetLogic().GetMRMLScene()

        if self._sourceFiducialList == None:
            
            # no list created yet
            self._sourceFiducialList = slicer.vtkMRMLFiducialListNode()
            self._sourceFiducialList.SetName("VMTK Fast Marching Source Points")
            self._sourceFiducialList.SetScene(scene)
            self._sourceFiducialList.SetColor(0.2,0.6,0.2)
            self._sourceFiducialList.SetLocked(1)
            scene.AddNode(self._sourceFiducialList)
            self._sourcePointsList.GetWidget().DeleteAll()

        #disable all other buttons
        self._parentClass.UnLockInitInterface(0)

        #change the button appeareance
        self._addSourcePointButton.SetActiveBackgroundColor(0.2,0.6,0.2)
        self._addSourcePointButton.SetReliefToSunken()
        self._addSourcePointButton.SetBackgroundColor(0.2,0.6,0.2)
        self._addSourcePointButton.SetForegroundColor(0.2,0.2,0.2)
        self._addSourcePointButton.SetText("Stop adding!")
        self._addSourcePointButton.SetWidth(15)
        self._addSourcePointButton.SetBalloonHelpString("Click to stop adding new source points")

        self._currentFiducialList = self._sourceFiducialList
        self._currentFiducialListLabel = "SP"
        self._parentClass.GetHelper().SetIsInteractiveMode(1,self)

        
    def TeardownAddSourcePoint(self):
    
        self._parentClass.GetHelper().SetIsInteractiveMode(0,None)

        #re-change the button appeareance
        self._addSourcePointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addSourcePointButton.SetReliefToRaised()
        self._addSourcePointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addSourcePointButton.SetForegroundColor(0.2,0.6,0.2)
        self._addSourcePointButton.SetText("Add Source Point")
        self._addSourcePointButton.SetWidth(15)
        self._addSourcePointButton.SetBalloonHelpString("Click to add new source point")

        self.UpdateGUIByState()
        self._parentClass.UpdateMRML()


    def InitAddTargetPoint(self):

        scene = self._parentClass.GetLogic().GetMRMLScene()

        if self._targetFiducialList == None:
            
            # no list created yet
            self._targetFiducialList = slicer.vtkMRMLFiducialListNode()
            self._targetFiducialList.SetName("VMTK Fast Marching Target Points")
            self._targetFiducialList.SetScene(scene)
            self._targetFiducialList.SetColor(0.2,0.2,0.6)
            self._targetFiducialList.SetLocked(1)
            scene.AddNode(self._targetFiducialList)
            self._targetPointsList.GetWidget().DeleteAll()

        #disable all other buttons
        self._parentClass.UnLockInitInterface(0)

        #change the button appeareance
        self._addTargetPointButton.SetActiveBackgroundColor(0.2,0.2,0.6)
        self._addTargetPointButton.SetReliefToSunken()
        self._addTargetPointButton.SetBackgroundColor(0.2,0.2,0.6)
        self._addTargetPointButton.SetForegroundColor(0.7,0.7,0.7)
        self._addTargetPointButton.SetActiveForegroundColor(0.7,0.7,0.7)
        self._addTargetPointButton.SetText("Stop adding!")
        self._addTargetPointButton.SetWidth(15)
        self._addTargetPointButton.SetBalloonHelpString("Click to stop adding new target points")

        self._currentFiducialList = self._targetFiducialList
        self._currentFiducialListLabel = "TP"
        self._parentClass.GetHelper().SetIsInteractiveMode(1,self)

        
    def TeardownAddTargetPoint(self):
    
        self._parentClass.GetHelper().SetIsInteractiveMode(0,None)

        #re-change the button appeareance
        self._addTargetPointButton.SetActiveBackgroundColor(0.9,0.9,0.9)
        self._addTargetPointButton.SetReliefToRaised()
        self._addTargetPointButton.SetBackgroundColor(0.9,0.9,0.9)
        self._addTargetPointButton.SetForegroundColor(0.2,0.2,0.6)
        self._addTargetPointButton.SetActiveForegroundColor(0.1,0.1,0.1)
        self._addTargetPointButton.SetText("Add Target Point")
        self._addTargetPointButton.SetWidth(15)
        self._addTargetPointButton.SetBalloonHelpString("Click to add new target point")

        self.UpdateGUIByState()
        self._parentClass.UpdateMRML()

    def RemoveSourcePoint(self):

        curSelectionId = self._sourcePointsList.GetWidget().GetSelectionIndex()

        if curSelectionId != -1:

            #at least one item selected, but which
            curSelection = self._sourcePointsList.GetWidget().GetSelection()

            if curSelection != "<no source points>":

                self._sourceFiducialList.RemoveFiducial(curSelectionId)


    def RemoveTargetPoint(self):

        curSelectionId = self._targetPointsList.GetWidget().GetSelectionIndex()

        if curSelectionId != -1:

            #at least one item selected, but which
            curSelection = self._targetPointsList.GetWidget().GetSelection()

            if curSelection != "<no target points>":

                self._targetFiducialList.RemoveFiducial(curSelectionId)


    #
    # coordinates are now RAS
    # which is the Name of the SliceWindow (Red,Yellow,Green)
    #
    def HandleClickInSliceWindowWithCoordinates(self, coordinates):
        SlicerVMTKAdvancedPageSkeleton.HandleClickInSliceWindowWithCoordinates(self, coordinates)

        coordinatesRAS = coordinates
        fiducial = self._currentFiducialList.AddFiducialWithXYZ(coordinatesRAS[0], coordinatesRAS[1], coordinatesRAS[2],0)

        numberOfFiducials = self._currentFiducialList.GetNumberOfFiducials()

        lastFiducial = 1

        # always use new Ids for the fiducial label
        if numberOfFiducials != 1:
            for i in range(0,numberOfFiducials-1):
                currentFiducialLabel = self._currentFiducialList.GetNthFiducialLabelText(i)
                currentFiducialLabel = currentFiducialLabel.split("P")[1]
                if int(currentFiducialLabel) >= lastFiducial:
                    lastFiducial = int(currentFiducialLabel)+1

        self._currentFiducialList.SetNthFiducialLabelText(fiducial, self._currentFiducialListLabel+str(lastFiducial))
        self._parentClass.GetHelper().debug("Fiducial Added! More to come!")

    #
    # Execute the algorithm
    #
    def Execute(self):

        self._parentClass.SetUpdatingOn()

        extentValues = self._thresholdSlider.GetExtent()
        if self._parentClass._initImageCheckbox.GetSelectedState()==1:
            inVolumeNode = self._parentClass._inVolumeSelectorSnd.GetSelected()
        else:
            inVolumeNode = self._parentClass._inVolumeSelector.GetSelected()
        lowerThreshold = extentValues[0]
        higherThreshold = extentValues[1]
        sourceSeedsNode = self._sourceFiducialList
        targetSeedsNode = self._targetFiducialList

        myLogic = self._parentClass.GetMyLogic()
        resultContainer = myLogic.ExecuteFastMarching(inVolumeNode,lowerThreshold,higherThreshold,sourceSeedsNode,targetSeedsNode)
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

        self._sourceFiducialList = None
        self._targetFiducialList = None
        self._currentFiducialList = None

        self.UpdateGUIByState()

