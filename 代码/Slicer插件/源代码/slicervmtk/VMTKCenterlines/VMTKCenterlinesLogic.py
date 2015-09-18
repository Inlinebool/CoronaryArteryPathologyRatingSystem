from Slicer import slicer

class VMTKCenterlinesLogic(object):

    def __init__(self,parentClass):

        self._parentClass = parentClass

        self._flipNormals = 0
        self._capDisplacement = 0.0
        self._radiusArrayName = 'MaximumInscribedSphereRadius'
        self._costFunction = '1/R'
        self._appendEndPoints = 0 
        
        self._resampling = 0
        self._resamplingStepLength = 1.0
        self._simplifyVoronoi = 0

        self._eikonalSolutionArrayName = 'EikonalSolution'
        self._edgeArrayName = 'EdgeArray'
        self._edgePCoordArrayName = 'EdgePCoordArray'
        self._costFunctionArrayName = 'costFunctionArray'

        self._vd = None

    def prepareModel(self,polydata):

        if polydata == None:
            return -1
        
        # skip nonmanifold

        surfaceCleaner = slicer.vtkCleanPolyData()
        surfaceCleaner.SetInput(polydata)
        surfaceCleaner.Update()

        surfaceTriangulator = slicer.vtkTriangleFilter()
        surfaceTriangulator.SetInput(surfaceCleaner.GetOutput())
        surfaceTriangulator.PassLinesOff()
        surfaceTriangulator.PassVertsOff()
        surfaceTriangulator.Update()

        # new steps for preparation to avoid problems because of slim models (f.e. at stenosis)
        subdiv = slicer.vtkLinearSubdivisionFilter()
        subdiv.SetInput(surfaceTriangulator.GetOutput())
        subdiv.SetNumberOfSubdivisions(1)
        subdiv.Update()

        smooth = slicer.vtkWindowedSincPolyDataFilter()
        smooth.SetInput(subdiv.GetOutput())
        smooth.SetNumberOfIterations(20)
        smooth.SetPassBand(0.1)
        smooth.SetBoundarySmoothing(1)
        smooth.NormalizeCoordinatesOn()
        smooth.Update()

        normals = slicer.vtkPolyDataNormals()
        normals.SetInput(smooth.GetOutput())
        normals.SetAutoOrientNormals(1)
        normals.SetFlipNormals(0)
        normals.SetConsistency(1)
        normals.SplittingOff()
        normals.Update()

        surfaceCapper = slicer.vtkvmtkCapPolyData()
        surfaceCapper.SetInput(normals.GetOutput())
        surfaceCapper.SetDisplacement(self._capDisplacement)
        surfaceCapper.SetInPlaneDisplacement(self._capDisplacement)
        surfaceCapper.Update()

        polyDataNew = slicer.vtkPolyData()
        polyDataNew.DeepCopy(surfaceCapper.GetOutput())
        polyDataNew.Update()

        return polyDataNew

    def computeCenterlines(self,polydata,inletSeedIds,outletSeedIds):


        centerlineFilter = slicer.vtkvmtkPolyDataCenterlines()
        centerlineFilter.SetInput(polydata)
        centerlineFilter.SetSourceSeedIds(inletSeedIds)
        centerlineFilter.SetTargetSeedIds(outletSeedIds)
        centerlineFilter.SetRadiusArrayName(self._radiusArrayName)
        centerlineFilter.SetCostFunction(self._costFunction)
        centerlineFilter.SetFlipNormals(self._flipNormals)
        centerlineFilter.SetAppendEndPointsToCenterlines(self._appendEndPoints)
        centerlineFilter.SetSimplifyVoronoi(self._simplifyVoronoi)
        centerlineFilter.SetCenterlineResampling(self._resampling)
        centerlineFilter.SetResamplingStepLength(self._resamplingStepLength)
        centerlineFilter.Update()

        polyDataNew = slicer.vtkPolyData()
        polyDataNew.DeepCopy(centerlineFilter.GetOutput())
        polyDataNew.Update()

        self._vd = slicer.vtkPolyData()
        self._vd.DeepCopy(centerlineFilter.GetVoronoiDiagram())
        self._vd.Update()

        return polyDataNew

    def GetVoronoiDiagram(self):



        return self._vd


    def Export(self,polyData,outputFileName,exportDetails,exportHeaders,exportNifti):

        f=open(outputFileName, 'w')
        line = "X Y Z"
        arrayNames = []
        dataArrays = polyData.GetPointData()

        if exportDetails==1:
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
        if exportHeaders == 1:
            f.write(line)
        numberOfLines = polyData.GetNumberOfPoints()

        for i in range(numberOfLines):
            point = polyData.GetPoint(numberOfLines - i - 1)
            if exportNifti==1:
                line = str(-1*point[0]) + ' ' + str(-1*point[1]) + ' ' + str(point[2])
            else:
                line = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            if exportDetails==1:
                for arrayName in arrayNames:
                    array = dataArrays.GetArray(arrayName)
                    for j in range(array.GetNumberOfComponents()):
                        line = line + ' ' + str(array.GetComponent(numberOfLines - i,j))
            line = line + '\n'
            f.write(line)

