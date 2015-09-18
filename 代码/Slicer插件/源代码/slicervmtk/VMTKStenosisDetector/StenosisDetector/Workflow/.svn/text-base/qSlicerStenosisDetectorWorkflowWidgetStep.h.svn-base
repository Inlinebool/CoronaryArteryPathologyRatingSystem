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

  This file was originally developed by
    Danielle Pace and Jean-Christophe Fillion-Robin, Kitware Inc.
  and was partially funded by NIH grant 3P41RR013218-12S1

==============================================================================*/

#ifndef __qSlicerStenosisDetectorWorkflowWidgetStep_h
#define __qSlicerStenosisDetectorWorkflowWidgetStep_h

// CTK includes
#include <ctkPimpl.h>
#include <ctkWorkflowWidgetStep.h>
#include <ctkWorkflowTransitions.h>

// SlicerQt includes
#include "qSlicerAbstractModuleWidget.h"
#include "qSlicerStenosisDetectorModuleExport.h"

class qSlicerStenosisDetectorWorkflowWidgetStepPrivate;



class Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT qSlicerStenosisDetectorWorkflowWidgetStep :
    public ctkWorkflowWidgetStep
{
  Q_OBJECT

public:

  typedef ctkWorkflowWidgetStep Superclass;
  explicit qSlicerStenosisDetectorWorkflowWidgetStep(ctkWorkflow* newWorkflow,
                                              const QString& newId, QWidget* newParent = 0);
  explicit qSlicerStenosisDetectorWorkflowWidgetStep(QWidget* newParent = 0);
  virtual ~qSlicerStenosisDetectorWorkflowWidgetStep();

  //vtkMRMLScene *           mrmlScene() const;
  //vtkEMSegmentMRMLManager* mrmlManager() const;

  //void setEMSegmentLogic(vtkSlicerEMSegmentLogic* logic);

public slots:
  //void setMRMLManager(vtkEMSegmentMRMLManager * newMRMLManager);

signals:


//protected:
  //vtkSlicerEMSegmentLogic* emSegmentLogic()const;

protected:
  QScopedPointer<qSlicerStenosisDetectorWorkflowWidgetStepPrivate> d_ptr;
//    QScopedPointer<qSlicerStenosisDetectorWorkflowWidgetStep> d_ptr;../Images/stenosiswelcome.png

private:
  Q_DECLARE_PRIVATE(qSlicerStenosisDetectorWorkflowWidgetStep);
  Q_DISABLE_COPY(qSlicerStenosisDetectorWorkflowWidgetStep);

};

#endif
