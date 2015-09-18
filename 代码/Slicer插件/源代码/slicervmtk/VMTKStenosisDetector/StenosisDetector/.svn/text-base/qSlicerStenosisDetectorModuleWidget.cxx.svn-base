/*==============================================================================

  Program: 3D Slicer

  Copyright (c) 2010 Kitware Inc.

  See Doc/copyright/copyright.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
  and was partially funded by NIH grant 3P41RR013218-12S1

==============================================================================*/

// Qt includes
#include <QDebug>
#include <QPushButton>

// EMSegment QTModule includes
#include "qSlicerStenosisDetectorModuleWidget.h"
#include "ui_qSlicerStenosisDetectorModule.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h"

// CTK includes
#include <ctkWorkflowStackedWidget.h>
#include <ctkWorkflowButtonBoxWidget.h>
#include <ctkWorkflowWidgetStep.h>
#include <ctkWorkflow.h>
#include <ctkWorkflowGroupBox.h>

// EMSegment QTModule includes
#include "Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep.h"
#include "Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep.h"

// STD includes
#include <cstdlib>


//-----------------------------------------------------------------------------
class qSlicerStenosisDetectorModuleWidgetPrivate: public Ui_qSlicerStenosisDetectorModule
{
  Q_DECLARE_PUBLIC(qSlicerStenosisDetectorModuleWidget);
protected:
  qSlicerStenosisDetectorModuleWidget* const q_ptr;
public:
  qSlicerStenosisDetectorModuleWidgetPrivate(qSlicerStenosisDetectorModuleWidget& object);
  ~qSlicerStenosisDetectorModuleWidgetPrivate();


  ctkWorkflow*                    Workflow;
  ctkWorkflowStackedWidget *      WorkflowWidget;

};

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorModuleWidgetPrivate methods

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorModuleWidgetPrivate::qSlicerStenosisDetectorModuleWidgetPrivate(qSlicerStenosisDetectorModuleWidget& object)
  : q_ptr(&object)
{
  this->Workflow = 0;
  this->WorkflowWidget = 0;
}
//
////-------------------------------------------------------------------------------
qSlicerStenosisDetectorModuleWidgetPrivate::~qSlicerStenosisDetectorModuleWidgetPrivate()
{
}


//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorModuleWidget methods

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorModuleWidgetPrivate methods ctkWorkflow*                    Workflow;
//ctkWorkflowStackedWidget *      WorkflowWidget;
//setupUi
//-----------------------------------------------------------------------------
//vtkSlicerEMSegmentLogic* qSlicerStenosisDetectorModuleWidgetPrivate::logic()const
//{http://www.cameroon-info.net/
  //Q_Q(const qSlicerStenosisDetectorModuleWidget);
  //return vtkSlicerEMSegmentLogic::SafeDownCast(q->logic());
//}

//-----------------------------------------------------------------------------
// qSlicerStenosisDetectorModuleWidget methods

//-----------------------------------------------------------------------------
const QString qSlicerStenosisDetectorModuleWidget::SimpleMode = "simple";
const QString qSlicerStenosisDetectorModuleWidget::AdvancedMode = "advanced";
// suares
//ctkWorkflow*                    Workflow;
// ctkWorkflowStackedWidget *      WorkflowWidget;

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorModuleWidget::qSlicerStenosisDetectorModuleWidget(QWidget* _parent)
  : Superclass(_parent)
//  , d_ptr(new qSlicerStenosisDetectorModuleWidget(*this))
, d_ptr(new qSlicerStenosisDetectorModuleWidgetPrivate(*this))
{
}

//-----------------------------------------------------------------------------
qSlicerStenosisDetectorModuleWidget::~qSlicerStenosisDetectorModuleWidget()
{
}

//-----------------------------------------------------------------------------
void qSlicerStenosisDetectorModuleWidget::setup()
{
	  Q_D(qSlicerStenosisDetectorModuleWidget);
	  d->setupUi(this);
  // create the workflow and workflow widget if necessary

  d->Workflow = new ctkWorkflow;

  d->WorkflowWidget = new ctkWorkflowStackedWidget(this);
  d->WorkflowWidget->setWorkflow(d->Workflow);
  d->gridLayout->addWidget(d->WorkflowWidget);


  QList<qSlicerStenosisDetectorWorkflowWidgetStep*> allSteps;

  // DefineTask Step is common to "simple" and "advanced" modes
//  qSlicerStenosisDetectorWorkflowWelcomeStep * welcomeStep =
  qSlicerStenosisDetectorWorkflowWidgetStep * welcomeStep =
      new qSlicerStenosisDetectorWorkflowWelcomeStep(d->Workflow);
  allSteps << welcomeStep;


  qSlicerStenosisDetectorWorkflowWidgetStep * selectVolumeStep =
      new qSlicerStenosisDetectorWorkflowSelectVolumeStep(d->Workflow);
  allSteps << selectVolumeStep;

  qSlicerStenosisDetectorWorkflowWidgetStep * vesselnessStep =
        new qSlicerStenosisDetectorWorkflowVesselnessStep(d->Workflow);
    allSteps << vesselnessStep;


    qSlicerStenosisDetectorWorkflowWidgetStep * lumenSegmentationStep =
          new qSlicerStenosisDetectorWorkflowLumenSegmentationStep(d->Workflow);
      allSteps << lumenSegmentationStep;

      qSlicerStenosisDetectorWorkflowWidgetStep * appreciationStep =
            new qSlicerStenosisDetectorWorkflowAppreciationStep(d->Workflow);
        allSteps << appreciationStep;

  // Initial step
  d->Workflow->setInitialStep(welcomeStep);

  d->Workflow->addTransition(welcomeStep, selectVolumeStep);
  d->Workflow->addTransition(selectVolumeStep, vesselnessStep);
  d->Workflow->addTransition(vesselnessStep, lumenSegmentationStep);
  d->Workflow->addTransition(lumenSegmentationStep, appreciationStep);

  // Add transition from DefineTask step to DefineInputChannelsAdvanced step
//  d->Workflow->addTransition(defineTaskStep, defineInputChannelsAdvancedStep,
//                             qSlicerStenosisDetectorModuleWidget::AdvancedMode);

  d->WorkflowWidget->buttonBoxWidget()->setBackButtonDefaultText("");
  d->WorkflowWidget->buttonBoxWidget()->setNextButtonDefaultText("");


  d->Workflow->start();
}

