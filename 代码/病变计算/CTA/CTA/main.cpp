#include "vtkPolyData.h"
#include "vtkPolyDataMapper.h"
#include "vtkCellData.h"
#include "vtkConeSource.h"
#include "vtkPolyDataReader.h"
#include "vtkPolyDataWriter.h"
#include "vtkActor.h"
#include "vtkRenderer.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkvmtkCenterlineGeometry.h"
#include "vtkvmtkDICOMImageReader.h"
#include "vtkFieldData.h"

int main()
{
	vtkPolyDataReader *polydataReader = vtkPolyDataReader::New();
	polydataReader->SetFileName("VMTKCenterlinesOut.vtk");
	polydataReader->Update();

	vtkPolyData *centerlinePolyData = vtkPolyData::New();
	centerlinePolyData = polydataReader->GetOutput();

	vtkvmtkCenterlineGeometry *centerlineGM = vtkvmtkCenterlineGeometry::New();
	centerlineGM->SetInput(centerlinePolyData);
	centerlineGM->SetLengthArrayName("Length");
	centerlineGM->SetCurvatureArrayName("Curvature");
	centerlineGM->SetTorsionArrayName("Torsion");
	centerlineGM->SetRadiusCurvatureArrayName("RadiusCurvature");
	centerlineGM->SetStenosisArrayName("Stenosis");
	centerlineGM->SetTortuosityArrayName("Tortuosity");
	centerlineGM->SetFrenetTangentArrayName("FrentTangent");
	centerlineGM->SetFrenetNormalArrayName("FrentNormal");
	centerlineGM->SetFrenetBinormalArrayName("FrentBinormal");
	centerlineGM->Update();
	centerlinePolyData = centerlineGM->GetOutput();

	vtkPolyDataWriter *polydataWriter = vtkPolyDataWriter::New();
	polydataWriter->SetInput(centerlinePolyData);
	polydataWriter->SetFileName("CenterlineGM1221.vtk");
	polydataWriter->Update();
	polydataWriter->Write();

	/*
	vtkPolyDataMapper *centerlineMapper = vtkPolyDataMapper::New();
	centerlineMapper->SetInputConnection(polydataReader->GetOutputPort());

	vtkActor *centerlineActor = vtkActor::New();
	centerlineActor->SetMapper(centerlineMapper);

	vtkRenderer *render = vtkRenderer::New();
	render->AddActor(centerlineActor);
	render->SetBackground(0.1,0.2,0.4);

	vtkRenderWindow *renWin = vtkRenderWindow::New();
	renWin->AddRenderer(render);
	renWin->SetSize(800,600);

	vtkRenderWindowInteractor *iren = vtkRenderWindowInteractor::New();
	iren->SetRenderWindow(renWin);

	iren->Initialize();
	iren->Start();

	//polydataReader->Delete();
	//centerlinePolyData->Delete();
	centerlineMapper->Delete();
	centerlineActor->Delete();
	render->Delete();
	renWin->Delete();
	iren->Delete();
	*/

	return 0;

}