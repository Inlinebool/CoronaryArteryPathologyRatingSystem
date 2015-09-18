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

  This file was originally developed by Danielle Pace, Kitware Inc.
  and was partially funded by NIH grant 3P41RR013218-12S1

==============================================================================*/

#ifndef __qSlicerStenosisDetectorWorkflowSelectVolumeStep_p
#define __qSlicerStenosisDetectorWorkflowSelectVolumeStep_p

// Qt includes
#include <QObject>

// CTK includes
#include <ctkPimpl.h>

// Qt includes
#include <QSignalMapper>
class QString;

// EMSegment includes
#include "Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.h"
//#include "ui_qSlicerStenosisDetectorWelcomeStep.h"
#include "ui_qSlicerStenosisDetectorSelectVolumeStep.h"

// MRML includes
class vtkMRMLNode;

//-----------------------------------------------------------------------------
class qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate : public QObject,
                                              public Ui_qSlicerStenosisDetectorSelectVolumeStep
{
  Q_OBJECT
  Q_DECLARE_PUBLIC(qSlicerStenosisDetectorWorkflowSelectVolumeStep)
protected:
  qSlicerStenosisDetectorWorkflowSelectVolumeStep* const q_ptr;
public:
  qSlicerStenosisDetectorWorkflowSelectVolumeStepPrivate(qSlicerStenosisDetectorWorkflowSelectVolumeStep& object);

  void setupUi(qSlicerStenosisDetectorWorkflowWidgetStep* step);

signals:


protected slots:

};

#endif
