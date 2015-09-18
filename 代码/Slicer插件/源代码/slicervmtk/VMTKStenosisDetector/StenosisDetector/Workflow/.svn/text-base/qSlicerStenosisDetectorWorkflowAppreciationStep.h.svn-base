#ifndef __qSlicerStenosisDetectorWorkflowAppreciationStep_h
#define __qSlicerStenosisDetectorWorkflowAppreciationStep_h

//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorAppreciationStep.h"

#include "qSlicerAbstractModuleWidget.h"

#include "qSlicerStenosisDetectorModuleExport.h"

#include "Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h"

class qSlicerStenosisDetectorWorkflowAppreciationStepPrivate;

class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT qSlicerStenosisDetectorWorkflowAppreciationStep : public qSlicerStenosisDetectorWorkflowWidgetStep
{
  Q_OBJECT

public:
  typedef qSlicerStenosisDetectorWorkflowWidgetStep Superclass;

  const static QString StepId;

  qSlicerStenosisDetectorWorkflowAppreciationStep(ctkWorkflow* newWorkflow, QWidget* parent = 0);
  ~qSlicerStenosisDetectorWorkflowAppreciationStep();

protected:
  QScopedPointer<qSlicerStenosisDetectorWorkflowAppreciationStepPrivate> d_ptr;
protected slots:


signals:


private:
  Q_DECLARE_PRIVATE(qSlicerStenosisDetectorWorkflowAppreciationStep);
  Q_DISABLE_COPY(qSlicerStenosisDetectorWorkflowAppreciationStep);

  // approved code starts here
  Ui::qSlicerStenosisDetectorAppreciationStep ui;

  // create the slot and signal connections
  void createConnection();

};

#endif
