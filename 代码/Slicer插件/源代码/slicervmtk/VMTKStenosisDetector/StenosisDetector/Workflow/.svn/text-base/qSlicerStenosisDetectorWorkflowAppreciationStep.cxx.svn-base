#include "Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep.h"
//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorAppreciationStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep_p.h"

// QT includes
#include <QButtonGroup>
#include <QList>
#include <QFontMetrics>
#include <QDebug>
#include <QMessageBox>
#include <QColorDialog>

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorWorkflowAppreciationStepPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorWorkflowAppreciationStepPrivate::qSlicerStenosisDetectorWorkflowAppreciationStepPrivate(qSlicerStenosisDetectorWorkflowAppreciationStep& object)
  : q_ptr(&object)
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorWorkflowAppreciationStepPrivate::setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step)
{
  this->Ui_qSlicerStenosisDetectorAppreciationStep::setupUi(step);
//    Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);

}


//-----------------------------------------------------------------------------
// qSlicerEMSegmentDefineTaskStep methods

//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorWorkflowAppreciationStep::StepId = "Finish";



qSlicerStenosisDetectorWorkflowAppreciationStep::~qSlicerStenosisDetectorWorkflowAppreciationStep()
{

}

qSlicerStenosisDetectorWorkflowAppreciationStep::qSlicerStenosisDetectorWorkflowAppreciationStep(
		  ctkWorkflow* newWorkflow, QWidget* newWidget)
		  : Superclass(newWorkflow, qSlicerStenosisDetectorWorkflowAppreciationStep::StepId, newWidget)
		  , d_ptr(new qSlicerStenosisDetectorWorkflowAppreciationStepPrivate(*this))
//          , d_ptr(this)
{
  Q_D(qSlicerStenosisDetectorWorkflowAppreciationStep);

  // now build the user interface
  d->setupUi(this);

  this->setName("4/4 - Evaluation");
  this->setDescription("Evaluation of the results");
  this->setButtonBoxHints(ctkWorkflowWidgetStep::NoHints);
  // create the slot and signal connections
  this->createConnection();
}

void qSlicerStenosisDetectorWorkflowAppreciationStep::createConnection()
{

}

