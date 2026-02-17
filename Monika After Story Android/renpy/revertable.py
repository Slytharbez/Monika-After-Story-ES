"""
COMPATIBILITY SHIM: renpy.revertable

Ren'Py 7.8.4 moved RevertableDict, RevertableList, and RevertableSet
from renpy.python to renpy.revertable. Persistent files saved by 7.8.4
embed 'renpy.revertable' class references in the pickle stream.

When Ren'Py 6.99.12 tries to unpickle these files, it fails with:
    ImportError: No module named revertable

This shim re-exports the classes from renpy.python so cPickle can
resolve the references during unpickling.
"""
from renpy.python import RevertableDict, RevertableList, RevertableSet
