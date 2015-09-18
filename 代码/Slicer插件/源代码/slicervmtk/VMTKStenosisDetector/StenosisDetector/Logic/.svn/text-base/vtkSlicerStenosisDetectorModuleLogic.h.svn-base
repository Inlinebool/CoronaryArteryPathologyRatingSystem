#ifndef __vtkSlicerStenosisDetectorModuleLogic_h
#define __vtkSlicerStenosisDetectorModuleLogic_h


// Slicer Logic includes
#include "vtkSlicerModuleLogic.h"

#include "vtkImageData.h"

#include "qSlicerStenosisDetectorModuleExport.h"

class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT vtkSlicerStenosisDetectorModuleLogic :
  public vtkSlicerModuleLogic
{
public:

  static vtkSlicerStenosisDetectorModuleLogic *New();
  vtkTypeRevisionMacro(vtkSlicerStenosisDetectorModuleLogic,vtkSlicerModuleLogic);
  virtual void PrintSelf(ostream& os, vtkIndent indent);

  vtkImageData* FrangiVesselEnhancement(vtkImageData* image, double minDiameter, double maxDiameter, double contrastOfImage);

protected:

  vtkSlicerStenosisDetectorModuleLogic();

  virtual ~vtkSlicerStenosisDetectorModuleLogic();

private:


};

#endif
