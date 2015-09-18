from Slicer import slicer

class VMTKBranchSplittingLogic(object):

  def __init__(self,parentClass):

    self._parentClass = parentClass
    self.Centerlines = None

    self._RadiusArrayName = 'MaximumInscribedSphereRadius'

    self._BlankingArrayName = 'Blanking'
    self._GroupIdsArrayName = 'GroupIds'
    self._CenterlineIdsArrayName = 'CenterlineIds'
    self._TractIdsArrayName = 'TractIds'
    self._advancementRatio = 1.05

    self._CutoffRadiusFactor = 1E16
    self._ClipValue = 0.0
    self._GroupIds = []
    self._InsideOut = 0
    self._UseRadiusInformation = 1
    self._vmtkRenderer = None
    self._OwnRenderer = 0
    self._Interactive = 0

  def branchSplitting(self,centerlines,model):
    self.Centerlines = centerlines

    self._parentClass._helper.debug("started branchExtractor")
    branchExtractor = slicer.vtkvmtkCenterlineBranchExtractor()
    branchExtractor.SetInput(centerlines)
    branchExtractor.SetBlankingArrayName(self._BlankingArrayName)
    branchExtractor.SetRadiusArrayName(self._RadiusArrayName)
    branchExtractor.SetGroupIdsArrayName(self._GroupIdsArrayName)
    branchExtractor.SetCenterlineIdsArrayName(self._CenterlineIdsArrayName)
    branchExtractor.SetTractIdsArrayName(self._TractIdsArrayName)
    branchExtractor.Update()
    self._parentClass._helper.debug("finished branchExtractor")
    self._parentClass._helper.debug("started clipper")
    clipper = slicer.vtkvmtkPolyDataCenterlineGroupsClipper()
    clipper.SetInput(model)
    clipper.SetCenterlines(branchExtractor.GetOutput())
    clipper.SetCenterlineGroupIdsArrayName(self._GroupIdsArrayName)
    clipper.SetGroupIdsArrayName(self._GroupIdsArrayName)
    clipper.SetCenterlineRadiusArrayName(self._RadiusArrayName)
    clipper.SetBlankingArrayName(self._BlankingArrayName)
    clipper.SetCutoffRadiusFactor(self._CutoffRadiusFactor)
    clipper.SetClipValue(self._ClipValue)
    clipper.SetUseRadiusInformation(self._UseRadiusInformation)
    clipper.ClipAllCenterlineGroupIdsOn()
    clipper.Update()
    self._parentClass._helper.debug("finished clipper")
    if not self._InsideOut:
      clipper.GenerateClippedOutputOff()
    else:
      clipper.GenerateClippedOutputOn()
    clipper.Update()

    if not self._InsideOut:
      Surface = clipper.GetOutput()
    else:
      Surface = clipper.GetClippedOutput()

    # shift values because first value is invisible in default LabelMap
    dataArray=Surface.GetPointData().GetScalars("GroupIds")
    newDa=slicer.vtkIntArray()
    newDa.SetName("GroupIds")
    newDa.InsertTuple1(0, 0)
    for i in range (1,dataArray.GetSize()):
      newDa.InsertTuple1(i, dataArray.GetValue(i)+1)

    polyDataNew = slicer.vtkPolyData()
    polyDataNew.DeepCopy(Surface)
    polyDataNew.GetPointData().SetScalars(newDa)
    polyDataNew.Update()

    return polyDataNew

  def splitModels(self,Surface):
    dataArray=Surface.GetPointData().GetScalars("GroupIds")
    scalarRange=dataArray.GetRange()
    
    newPdList=[]
    newCaList=[]
    self._parentClass._helper.debug("started splitter")
    # generate containers CellArray & PolyData + copy points
    for i in range(1,int(scalarRange[1])+2):
      newCellArray=slicer.vtkCellArray()
      newPolyData=slicer.vtkPolyData()

      points=slicer.vtkPoints()
      points.DeepCopy(Surface.GetPoints())		
      newPolyData.SetPoints(points)
      newPolyData.SetPolys(newCellArray)
      newPolyData.Update()

      newPdList.append(newPolyData)
      newCaList.append(newCellArray)

    #Fill containers with Polys
    for i in range (0,Surface.GetPolys().GetNumberOfCells()):
      poi=Surface.GetCell(i).GetPointIds()

      if(poi.GetNumberOfIds()==0):
        continue

      scalarsOfPoints =[]
  
      for pid in range(0,poi.GetNumberOfIds()): 
        p=poi.GetId(pid)
        scalarsOfPoints.append(dataArray.GetValue(p))

      max=0
      largestIndex=0
      for j in range(1,int(scalarRange[1])+2):
        c=scalarsOfPoints.count(j)
        if c >= max:
          max=c
          largestIndex=j
      newCaList[largestIndex].InsertNextCell(Surface.GetCell(i))

    # clean PolyData
    for pd in newPdList:
      cleanPolyData = slicer.vtkCleanPolyData();
      cleanPolyData.SetInput(pd);
      cleanPolyData.Update();
      pd.DeepCopy(cleanPolyData.GetOutput())
      
    self._parentClass._helper.debug("finished splitter")

    return newPdList

