from Slicer import slicer

class VMTKNetworkExtractionLogic(object):

    def __init__(self,parentClass):

        self._parentClass = parentClass
        self._radiusArrayName = 'MaximumInscribedSphereRadius'
        self._topologyArrayName = 'Topology'
        self._marksArrayName = 'Marks'

        self._advancementRatio = 1.05

    def extractNetwork(self,polydata,seed):

        surfaceTriangulator = slicer.vtkTriangleFilter()
        surfaceTriangulator.SetInput(polydata)
        surfaceTriangulator.PassLinesOff()
        surfaceTriangulator.PassVertsOff()
        surfaceTriangulator.Update()

        # new steps for preparation to avoid problems because of slim models (f.e. at stenosis)
        subdiv = slicer.vtkLinearSubdivisionFilter()
        subdiv.SetInput(surfaceTriangulator.GetOutput())
        subdiv.SetNumberOfSubdivisions(1)
        subdiv.Update()

        # now close the surface
        surfaceCapper = slicer.vtkvmtkCapPolyData()                                                                                                                  
        surfaceCapper.SetInput(subdiv.GetOutput())                                                                                                                  
        surfaceCapper.SetDisplacement(0.0)                                                                                                         
        surfaceCapper.SetInPlaneDisplacement(0.0)                                                                                                  
        surfaceCapper.Update() 

        # re-open it where the seed is placed
        someradius = 1.0

        surface=surfaceCapper.GetOutput()

        pointLocator = slicer.vtkPointLocator()                                                                                                                  
        pointLocator.SetDataSet(surface)                                                                                                           
        pointLocator.BuildLocator() 

        id=pointLocator.FindClosestPoint(int(seed[0]),int(seed[1]),int(seed[2]))

        seed = surface.GetPoint(id)

        sphere = slicer.vtkSphere()
        sphere.SetCenter(seed[0],seed[1],seed[2])
        sphere.SetRadius(someradius)

        clip = slicer.vtkClipPolyData()
        clip.SetInput(surface)
        clip.SetClipFunction(sphere)
        clip.Update()

        opensurface = clip.GetOutput()

        networkExtraction = slicer.vtkvmtkPolyDataNetworkExtraction()                                                                    
        networkExtraction.SetInput(opensurface)                                                                                          
        networkExtraction.SetAdvancementRatio(self._advancementRatio)                                                                      
        networkExtraction.SetRadiusArrayName(self._radiusArrayName)                                                                        
        networkExtraction.SetTopologyArrayName(self._topologyArrayName)                                                                    
        networkExtraction.SetMarksArrayName(self._marksArrayName)                                                                          
        networkExtraction.Update()

        self._parentClass._helper.debug(self._topologyArrayName)

        network=networkExtraction.GetOutput()
        arrayNames = []
        celldata = network.GetCellData()

        for i in range(celldata.GetNumberOfArrays()):                                                                                                      
            array = celldata.GetArray(i)                                                                                                                   
            arrayName = array.GetName()                                                                                                                      
            if arrayName == None:                                                                                                                            
                continue                                                                                                                                     
            if (arrayName[-1]=='_'):                                                                                                                         
                continue                                                                                                                                     
            arrayNames.append(arrayName)

        numberOfPoints = network.GetNumberOfPoints()

        for i in range(numberOfPoints):

            point = network.GetPoint(numberOfPoints - i - 1)

            line = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            for arrayName in arrayNames:                                                                                                                     
                array = celldata.GetArray(arrayName)                                                                                                       
                for j in range(array.GetNumberOfComponents()):                                                                                               
                    line = line + ' ' + arrayName + ": " + str(array.GetComponent(numberOfPoints - i,j))                                                                         

            self._parentClass._helper.debug(line)

        polyDataNew = slicer.vtkPolyData()
        polyDataNew.DeepCopy(network)
        polyDataNew.Update()

        return polyDataNew
