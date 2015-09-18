#include "Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep.h"
//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorVesselnessStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep_p.h"

// QT includes
#include <QButtonGroup>
#include <QList>
#include <QFontMetrics>
#include <QDebug>
#include <QMessageBox>
#include <QColorDialog>

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorWorkflowVesselnessStepPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorWorkflowVesselnessStepPrivate::qSlicerStenosisDetectorWorkflowVesselnessStepPrivate(qSlicerStenosisDetectorWorkflowVesselnessStep& object)
  : q_ptr(&object)
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorWorkflowVesselnessStepPrivate::setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step)
{
  this->Ui_qSlicerStenosisDetectorVesselnessStep::setupUi(step);
//    Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);

}


//-----------------------------------------------------------------------------
// qSlicerEMSegmentDefineTaskStep methods

//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorWorkflowVesselnessStep::StepId = "fix vesselness";



qSlicerStenosisDetectorWorkflowVesselnessStep::~qSlicerStenosisDetectorWorkflowVesselnessStep()
{

}

qSlicerStenosisDetectorWorkflowVesselnessStep::qSlicerStenosisDetectorWorkflowVesselnessStep(
		  ctkWorkflow* newWorkflow, QWidget* newWidget)
		  : Superclass(newWorkflow, qSlicerStenosisDetectorWorkflowVesselnessStep::StepId, newWidget)
		  , d_ptr(new qSlicerStenosisDetectorWorkflowVesselnessStepPrivate(*this))
//          , d_ptr(this)
{
  Q_D(qSlicerStenosisDetectorWorkflowVesselnessStep);
//  checked=false;
  // now build the user interface
  d->setupUi(this);
//  checked= d->checkBox->isChecked();

  this->setName("2/4 - Vesselness");
  this->setDescription("Preview appreciation for one slice and vessel contrast set");
  this->setButtonBoxHints(ctkWorkflowWidgetStep::NoHints);
//  connect(d->checkBox, SIGNAL(stateChanged(int)), this, SLOT(advandedHandel()));
  // create the slot and signal connections
  this->createConnection();
}

void qSlicerStenosisDetectorWorkflowVesselnessStep::createConnection()
{

}

//void qSlicerStenosisDetectorWorkflowVesselnessStepPrivate::advandedHandel()
//{
////	bool checked = d->checkBox->isChecked();
//	if(this->checkBox->isChecked())	{
////		this->widget
//	}
//	else{
//	}
//}

