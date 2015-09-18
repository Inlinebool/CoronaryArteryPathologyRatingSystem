from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000

###
### welcome page (derived from skeleton)
###
class SlicerVMTKInitializationWelcomeGUI(SlicerVMTKAdvancedPageSkeleton):

    def __init__(self,parentFrame,parentClass):
        SlicerVMTKAdvancedPageSkeleton.__init__(self,parentFrame,parentClass)

        self._welcomeMessage = slicer.vtkKWTextWithHyperlinksWithScrollbars()

    def Destructor(self):
        SlicerVMTKAdvancedPageSkeleton.Destructor(self)

        self._welcomeMessage = None

    def BuildGUI(self):
        SlicerVMTKAdvancedPageSkeleton.BuildGUI(self)


        self._welcomeMessage.SetParent(self._parentFrame)
        self._welcomeMessage.Create()
        self._welcomeMessage.GetWidget().SetWrapToWord()
        self._welcomeMessage.GetWidget().SetHeight(15)
        self._welcomeMessage.GetWidget().QuickFormattingOn()
        self._welcomeMessage.SetHorizontalScrollbarVisibility(0)
        self._welcomeMessage.SetVerticalScrollbarVisibility(1)
        self._welcomeMessage.SetText("**Level-Set Segmentation using VMTK** (<a>http://www.vmtk.org</a>):\n\n\nThe following initialization methods exist:\n\n**Colliding Fronts**: very effective when it is necessary to initialize the tract of a vessel, side branches will be ignored.\n\n**Fast Marching**: effective when it is necessary to segment round objects such as aneurysms. For example, by simply placing one seed at the center and one target on the wall, the volume will be initialized.\n\n**Threshold**: pixels comprised within two specified thresholds will be selected as the initial level sets.\n\n**Isosurface**: initial level sets will correspond to an isosurface of the image with sub-pixel precision.\n\n**Seeds**: initial deformable model is chosen by placing seeds.")
        self._welcomeMessage.GetWidget().ReadOnlyOn()


        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._welcomeMessage.GetWidgetName(),self._parentFrame.GetWidgetName()))



