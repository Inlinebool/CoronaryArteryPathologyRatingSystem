// Annotation includes
#include "Logic/vtkSlicerStenosisDetectorModuleLogic.h"


// MRML includes
#include <vtkMRMLScene.h>

// VTK includes
#include <vtkSmartPointer.h>
#include <vtkImageData.h>
#include <vtkImageCast.h>
#include <vtkPointData.h>
#include <vtkDataArray.h>

//vmtk inlcudes
#include "vtkVmtk/Segmentation/vtkvmtkVesselnessMeasureImageFilter.h"
//#include "vtkvmtkVesselnessMeasureImageFilter.h"

// STD includes
#include <string>
#include <iostream>
#include <sstream>

// Convenient macro
#define VTK_CREATE(type, name) \
  vtkSmartPointer<type> name = vtkSmartPointer<type>::New()

//-----------------------------------------------------------------------------
vtkCxxRevisionMacro(vtkSlicerStenosisDetectorModuleLogic, "$Revision: 1.0$")
vtkStandardNewMacro(vtkSlicerStenosisDetectorModuleLogic)

//-----------------------------------------------------------------------------
void vtkSlicerStenosisDetectorModuleLogic::PrintSelf(ostream& os, vtkIndent indent)
{
  Superclass::PrintSelf(os, indent);
}


//-----------------------------------------------------------------------------
// vtkSlicerAnnotationModuleLogic methods
//-----------------------------------------------------------------------------
vtkSlicerStenosisDetectorModuleLogic::vtkSlicerStenosisDetectorModuleLogic()
{

}

//-----------------------------------------------------------------------------
vtkSlicerStenosisDetectorModuleLogic::~vtkSlicerStenosisDetectorModuleLogic()
{

}

//-----------------------------------------------------------------------------
vtkImageData* vtkSlicerStenosisDetectorModuleLogic::FrangiVesselEnhancement(vtkImageData* image, double minDiameter, double maxDiameter, double contrastOfImage)
{
  vtkImageCast* cast = vtkImageCast::New();
  cast->SetInput(image);
  cast->SetOutputScalarTypeToFloat();
  cast->Update();
  image = cast->GetOutput();
  cast->Delete();

  vtkvmtkVesselnessMeasureImageFilter* v = vtkvmtkVesselnessMeasureImageFilter::New();
  v->SetInput(image);
  v->SetSigmaMin(minDiameter);
  v->SetSigmaMax(maxDiameter);
  v->SetNumberOfSigmaSteps(10);
  v->SetAlpha(0.3);
  v->SetBeta(500);
  v->SetGamma(contrastOfImage);
  v->Update();
  v->Delete();

  vtkImageData* outVolumeData = vtkImageData::New();
  outVolumeData->DeepCopy(v->GetOutput());
  outVolumeData->Update();
  outVolumeData->GetPointData()->GetScalars()->Modified();
  outVolumeData->Delete();

  return outVolumeData;

}
