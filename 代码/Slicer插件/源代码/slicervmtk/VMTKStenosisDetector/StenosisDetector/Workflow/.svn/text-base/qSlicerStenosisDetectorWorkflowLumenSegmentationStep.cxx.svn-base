#include "Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep.h"
//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorLumenSegmentationStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep_p.h"

// QT includes
#include <QButtonGroup>
#include <QList>
#include <QFontMetrics>
#include <QDebug>
#include <QMessageBox>
#include <QColorDialog>

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate::qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate(qSlicerStenosisDetectorWorkflowLumenSegmentationStep& object)
  : q_ptr(&object)
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate::setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step)
{
  this->Ui_qSlicerStenosisDetectorLumenSegmentationStep::setupUi(step);
//    Ui_qSlicerStenosisDetectorWelcomeStep::setupUi(step);

}


//-----------------------------------------------------------------------------
// qSlicerEMSegmentDefineTaskStep methods

//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorWorkflowLumenSegmentationStep::StepId = "set segmentation";



qSlicerStenosisDetectorWorkflowLumenSegmentationStep::~qSlicerStenosisDetectorWorkflowLumenSegmentationStep()
{

}

qSlicerStenosisDetectorWorkflowLumenSegmentationStep::qSlicerStenosisDetectorWorkflowLumenSegmentationStep(
		  ctkWorkflow* newWorkflow, QWidget* newWidget)
		  : Superclass(newWorkflow, qSlicerStenosisDetectorWorkflowLumenSegmentationStep::StepId, newWidget)
		  , d_ptr(new qSlicerStenosisDetectorWorkflowLumenSegmentationStepPrivate(*this))
//          , d_ptr(this)
{
  Q_D(qSlicerStenosisDetectorWorkflowLumenSegmentationStep);

  // now build the user interface
  d->setupUi(this);

  this->setName("3/4 - Lumen segmentation");
  this->setDescription("Thresholding set");
  this->setButtonBoxHints(ctkWorkflowWidgetStep::NoHints);

  // create the slot and signal connections
  this->createConnection();
}

void qSlicerStenosisDetectorWorkflowLumenSegmentationStep::createConnection()
{

}

