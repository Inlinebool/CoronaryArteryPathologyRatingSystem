from SlicerVMTKAdvancedPageSkeleton import SlicerVMTKAdvancedPageSkeleton
from Slicer import slicer

vtkKWPushButton_InvokedEvent = 10000

###
### curves evolution (derived from skeleton)
###
class SlicerVMTKEvolutionWelcomeGUI(SlicerVMTKAdvancedPageSkeleton):

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
        self._welcomeMessage.SetText("**Level-Set Segmentation using VMTK** (<a>http://www.vmtk.org</a>):\n\n\nThe following evolution methods exist:\n\n**Geodesic**: evolution using the geodesic active contour filter\n\n**Curves**: evolution using the curves image filter\n\n**Parameters**:\n**Number of iterations** is the number of deformation steps the model will perform.\n\n**Propagation scaling** is the weight you assign to model inflation.\n\n**Curvature scaling** is the weight you assign to model surface regularization\n\n**Advection scaling** regulates the attraction of the surface of the image gradient modulus ridges")
        self._welcomeMessage.GetWidget().ReadOnlyOn()


        slicer.TkCall("pack %s -side top -anchor nw -fill x -padx 2 -pady 2 -in %s" % (self._welcomeMessage.GetWidgetName(),self._parentFrame.GetWidgetName()))



