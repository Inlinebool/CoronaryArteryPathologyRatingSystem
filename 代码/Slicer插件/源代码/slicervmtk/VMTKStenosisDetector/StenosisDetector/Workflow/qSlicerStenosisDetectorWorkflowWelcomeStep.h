#ifndef __qSlicerStenosisDetectorWorkflowWelcomeStep_h
#define __qSlicerStenosisDetectorWorkflowWelcomeStep_h

#include "ui_qSlicerStenosisDetectorWelcomeStep.h"

#include "qSlicerAbstractModuleWidget.h"

#include "qSlicerStenosisDetectorModuleExport.h"

#include "Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h"

 class qSlicerStenosisDetectorWorkflowWelcomeStepPrivate;

class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT qSlicerStenosisDetectorWorkflowWelcomeStep : public qSlicerStenosisDetectorWorkflowWidgetStep
{
  Q_OBJECT

public:
  typedef qSlicerStenosisDetectorWorkflowWidgetStep Superclass;

  const static QString StepId;

  qSlicerStenosisDetectorWorkflowWelcomeStep(ctkWorkflow* newWorkflow, QWidget* parent = 0);
  ~qSlicerStenosisDetectorWorkflowWelcomeStep();

protected:
  QScopedPointer<qSlicerStenosisDetectorWorkflowWelcomeStepPrivate> d_ptr;
//    QScopedPointer<qSlicerStenosisDetectorWorkflowWelcomeStep> d_ptr;
protected slots:


signals:



private:
  Q_DECLARE_PRIVATE(qSlicerStenosisDetectorWorkflowWelcomeStep);
  Q_DISABLE_COPY(qSlicerStenosisDetectorWorkflowWelcomeStep);

  // approved code starts here
  Ui::qSlicerStenosisDetectorWelcomeStep ui;

  // create the slot and signal connections
  void createConnection();

};

#endif
