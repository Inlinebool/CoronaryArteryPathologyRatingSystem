from Slicer import slicer
from time import strftime
from math import floor

class VMTKCenterlinesHelper(object):

    def __init__(self,parentClass):

        self._parentClass = parentClass

    def debug(self,msg):

        '''debug prints to stdout (better than print because of flush)'''

        # declaration of new variable without type specification
        debugMode = 0

        if debugMode: # debugMode is a bool

            # the print statement needs strings as input, so every value to output has to be
            # casted
            print "[VMTKCenterlines " + strftime("%H:%M:%S") + "] " + str(msg)
            import sys
            sys.stdout.flush()

