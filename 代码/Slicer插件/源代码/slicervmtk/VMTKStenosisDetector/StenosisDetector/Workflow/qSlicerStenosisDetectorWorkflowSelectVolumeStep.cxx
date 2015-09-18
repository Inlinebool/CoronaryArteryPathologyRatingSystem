#include "Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.h"
//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorSelectVolumeStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep_p.h"

// QT includes
#include <QButtonGroup>
#include <QList>
#include <QFontMetrics>
#include <QDebug>
#include <QMessageBox>
#include <QColorDialog>

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate::qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate(qSlicerStenosisDetectorWorkflowSelectVolumeStep& object)
  : q_ptr(&object)
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate::setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step)
{
  this->Ui_qSlicerStenosisDetectorSelectVolumeStep::setupUi(step);
//    Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);

}


//-----------------------------------------------------------------------------
// qSlicerEMSegmentDefineTaskStep methods

//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorWorkflowSelectVolumeStep::StepId = "Select Volume";



qSlicerStenosisDetectorWorkflowSelectVolumeStep::~qSlicerStenosisDetectorWorkflowSelectVolumeStep()
{

}

qSlicerStenosisDetectorWorkflowSelectVolumeStep::qSlicerStenosisDetectorWorkflowSelectVolumeStep(
		  ctkWorkflow* newWorkflow, QWidget* newWidget)
		  : Superclass(newWorkflow, qSlicerStenosisDetectorWorkflowSelectVolumeStep::StepId, newWidget)
		  , d_ptr(new qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate(*this))
//          , d_ptr(this)
{
  Q_D(qSlicerStenosisDetectorWorkflowSelectVolumeStep);

  // now build the user interface
  d->setupUi(this);

  this->setName("1/4 - Input Volume");
  this->setDescription("Select the input Volume an fix the seed");
  this->setButtonBoxHints(ctkWorkflowWidgetStep::NoHints);

  // create the slot and signal connections
  this->createConnection();
}

void qSlicerStenosisDetectorWorkflowSelectVolumeStep::createConnection()
{

}

