#ifndef __qSlicerStenosisDetectorWorkflowSelectVolumeStep_h
#define __qSlicerStenosisDetectorWorkflowSelectVolumeStep_h

//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorSelectVolumeStep.h"

#include "qSlicerAbstractModuleWidget.h"

#include "qSlicerStenosisDetectorModuleExport.h"

#include "Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h"

class qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate;

class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT qSlicerStenosisDetectorWorkflowSelectVolumeStep : public qSlicerStenosisDetectorWorkflowWidgetStep
{
  Q_OBJECT

public:
  typedef qSlicerStenosisDetectorWorkflowWidgetStep Superclass;

  const static QString StepId;

  qSlicerStenosisDetectorWorkflowSelectVolumeStep(ctkWorkflow* newWorkflow, QWidget* parent = 0);
  ~qSlicerStenosisDetectorWorkflowSelectVolumeStep();

protected:
  QScopedPointer<qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate> d_ptr;
protected slots:


signals:



private:
  Q_DECLARE_PRIVATE(qSlicerStenosisDetectorWorkflowSelectVolumeStep);
  Q_DISABLE_COPY(qSlicerStenosisDetectorWorkflowSelectVolumeStep);

  // approved code starts here
  Ui::qSlicerStenosisDetectorSelectVolumeStep ui;

  // create the slot and signal connections
  void createConnection();

};

#endif
