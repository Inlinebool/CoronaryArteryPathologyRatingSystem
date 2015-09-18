#include "Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep_p.h"

// QT includes
#include <QButtonGroup>
#include <QList>
#include <QFontMetrics>
#include <QDebug>
#include <QMessageBox>
#include <QColorDialog>


//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorWorkflowWelcomeStepPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorWorkflowWelcomeStepPrivate::qSlicerStenosisDetectorWorkflowWelcomeStepPrivate(qSlicerStenosisDetectorWorkflowWelcomeStep& object)
  : q_ptr(&object)
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorWorkflowWelcomeStepPrivate::setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step)
{
  this->Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);
//  Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);
}


//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorDefineTaskStep methods
 // ui.lockUnlockButton->setIcon(QIcon(":/Icons/AnnotationLock.png"));
//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorWorkflowWelcomeStep::StepId = "welcome";



qSlicerStenosisDetectorWorkflowWelcomeStep::~qSlicerStenosisDetectorWorkflowWelcomeStep()
{

}

qSlicerStenosisDetectorWorkflowWelcomeStep::qSlicerStenosisDetectorWorkflowWelcomeStep(
		  ctkWorkflow* newWorkflow, QWidget* newWidget)
		  : Superclass(newWorkflow, qSlicerStenosisDetectorWorkflowWelcomeStep::StepId, newWidget)
//		  , d_ptr(this)
		  , d_ptr(new qSlicerStenosisDetectorWorkflowWelcomeStepPrivate(*this))
{
  Q_D(qSlicerStenosisDetectorWorkflowWelcomeStep);

  // now build the user interface
  d->setupUi(this);

  this->setName("Welcome");
  this->setDescription("Welcome page");
  this->setButtonBoxHints(ctkWorkflowWidgetStep::BackButtonDisabled);


  // create the slot and signal connections
  this->createConnection();
}

void qSlicerStenosisDetectorWorkflowWelcomeStep::createConnection()
{

}

