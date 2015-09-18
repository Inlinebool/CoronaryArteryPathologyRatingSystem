# uses epydoc
epydoc -o doc --html --exclude=SlicerScriptedModule* -n SlicerVMTKLevelSet -u http://www.nitrc.org/projects/slicervmtklvlst/ --separate-classes --graph=umlclasstree *.py
