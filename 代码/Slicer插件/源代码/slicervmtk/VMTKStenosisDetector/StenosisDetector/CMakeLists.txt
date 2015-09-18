#-----------------------------------------------------------------------
#
# SETUP
#
#-----------------------------------------------------------------------
# Module name (usually identique to the directory name)
SET(qt_module_name "StenosisDetector")

SET(qt_module_title "StenosisDetector")

SET(qt_module_export_directive "Q_SLICER_QTMODULES_STENOSISDETECTOR_EXPORT")

# Additional includes - Current_{source,binary} and Slicer_{Libs,Base} already included
#SET(qt_module_include_directories
#  ${CMAKE_CURRENT_SOURCE_DIR}/Widgets
#  ${CMAKE_CURRENT_SOURCE_DIR}/MRML
#  )

#-----------------------------------------------------------------------
#
# LOGIC
#
#-----------------------------------------------------------------------
SET(Logic_SRCS
  Logic/vtkSlicerStenosisDetectorModuleLogic.h
  Logic/vtkSlicerStenosisDetectorModuleLogic.cxx
  )
  
#-----------------------------------------------------------------------
#
# WORKFLOW
#
#-----------------------------------------------------------------------
SET(Workflow_SRCS
  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep.h
  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.h
  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep.h
  Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep.h
  Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep.h
  Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.cxx
  Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h  
  )
    
  
  
#-----------------------------------------------------------------------
#
# GUI
#
#  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep_p.h  
#-----------------------------------------------------------------------
SET(GUI_SRCS
  qSlicerStenosisDetectorModuleWidget.cxx
  qSlicerStenosisDetectorModuleWidget.h  
  )
#  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep_p.h  



#-----------------------------------------------------------------------
#
# ALL SOURCE FILES TOGETHER
#
#-----------------------------------------------------------------------
SET(qt_module_SRCS
  ${Logic_SRCS}
  ${GUI_SRCS}
  ${Workflow_SRCS}
  qSlicerStenosisDetectorModule.cxx
  qSlicerStenosisDetectorModule.h
  )



#-----------------------------------------------------------------------
#
# MOC HEADERS
#
#-----------------------------------------------------------------------
SET(qt_module_MOC_SRCS
  qSlicerStenosisDetectorModule.h
  qSlicerStenosisDetectorModuleWidget.h
  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep.h
  Workflow/qSlicerStenosisDetectorWorkflowWelcomeStep_p.h 
  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep.h   
  Workflow/qSlicerStenosisDetectorWorkflowSelectVolumeStep_p.h    
  Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep.h
  Workflow/qSlicerStenosisDetectorWorkflowVesselnessStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep.h
  Workflow/qSlicerStenosisDetectorWorkflowLumenSegmentationStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep.h
  Workflow/qSlicerStenosisDetectorWorkflowAppreciationStep_p.h  
  Workflow/qSlicerStenosisDetectorWorkflowWidgetStep.h
  )

#-----------------------------------------------------------------------
#
# RESOURCES
#
#-----------------------------------------------------------------------
SET(qt_module_UI_SRCS
  Resources/UI/qSlicerStenosisDetectorModule.ui
  Resources/UI/qSlicerStenosisDetectorWelcomeStep.ui
  Resources/UI/qSlicerStenosisDetectorSelectVolumeStep.ui
  Resources/UI/qSlicerStenosisDetectorVesselnessStep.ui
  Resources/UI/qSlicerStenosisDetectorLumenSegmentationStep.ui
  Resources/UI/qSlicerStenosisDetectorAppreciationStep.ui
  )
#-----------------------------------------------------------------------
#
# LINK TARGETS
#Welcome
#-----------------------------------------------------------------------
# Additional Target libraries
SET(qt_module_target_libraries
  qSlicerBaseQTCore
  qMRMLWidgets
)

# VMTK SETTINGS
set(VTK_VMTK_CONTRIB OFF) # no user contribs
set(VTK_VMTK_IN_SLICER ON) # activate Slicer install switch
set(TETGEN_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/vtkVmtk/Utilities/tetgen1.4.3) # fix

set(VTK_VMTK_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/vtkVmtk)

subdirs(
  vtkVmtk
)
# END VMTK SETTINGS

#-----------------------------------------------------------------------
#
# BUILD QTMODULE
#
#-----------------------------------------------------------------------
slicerMacroBuildQtModule(
  NAME ${qt_module_name}
  TITLE ${qt_module_title}
  EXPORT_DIRECTIVE ${qt_module_export_directive}
  INCLUDE_DIRECTORIES ${qt_module_include_directories} vtkVmtk
  SRCS ${qt_module_SRCS}
  MOC_SRCS ${qt_module_MOC_SRCS}
  UI_SRCS ${qt_module_UI_SRCS}
  TARGET_LIBRARIES ${qt_module_target_libraries}
  RESOURCES ${qt_module_resources}
)

#-----------------------------------------------------------------------
#
# TESTING
#
#-----------------------------------------------------------------------
if(BUILD_TESTING)
  #ADD_SUBDIRECTORY(Testing/Cxx)
endif(BUILD_TESTING)

