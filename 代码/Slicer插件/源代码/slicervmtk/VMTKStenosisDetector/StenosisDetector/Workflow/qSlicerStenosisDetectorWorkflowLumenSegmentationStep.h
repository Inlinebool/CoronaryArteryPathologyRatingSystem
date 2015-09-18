#ifndef __qSlicerStenosisDetectorWorkflowLumenSegmentationStep_h
#define __qSlicerStenosisDetectorWorkflowLumenSegmentationStep_h

//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorLumenSegmentationStep.h"

#include "qSlicerAbstractModuleWidget.h"

#include "qSlicerStenosisDetectorModuleExport.h"

#include "Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h"

class qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate;

class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT qSlicerStenosisDetectorWorkflowLumenSegmentationStep : public qSlicerStenosisDetectorWorkflowWidgetStep
{
  Q_OBJECT

public:
  typedef qSlicerStenosisDetectorWorkflowWidgetStep Superclass;

  const static QString StepId;

  qSlicerStenosisDetectorWorkflowLumenSegmentationStep(ctkWorkflow* newWorkflow, QWidget* parent = 0);
  ~qSlicerStenosisDetectorWorkflowLumenSegmentationStep();

protected:
  QScopedPointer<qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate> d_ptr;
protected slots:


signals:



private:
  Q_DECLARE_PRIVATE(qSlicerStenosisDetectorWorkflowLumenSegmentationStep);
  Q_DISABLE_COPY(qSlicerStenosisDetectorWorkflowLumenSegmentationStep);

  // approved code starts here
  Ui::qSlicerStenosisDetectorLumenSegmentationStep ui;

  // create the slot and signal connections
  void createConnection();

};

#endif
