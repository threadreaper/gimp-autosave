#!/usr/bin/env python
#Original (by yahvuu): http://www.gimpusers.com/forums/gimp-developer/11718-autosave-plugin
import tempfile
import os
from time import *
from gimpfu import *
def autosave(image, layer):
    backupInterval = 300
    backupFiles = {}
    print("Autosave activated")
    while 1:
        sleep(backupInterval)
        print(ctime(time()))
        curImages = {}
        for k in gimp.image_list():
            curImages[k.ID] = k
            curIDs = curImages.keys()
            oldIDs = backupFiles.keys()
            newIDs = [x for x in curIDs if x not in oldIDs]
            delIDs = [x for x in oldIDs if x not in curIDs]
        for id in newIDs:
            prefix = 'gimpbackup-ID%s-' % str(id)
            fn = tempfile.mkstemp(prefix=prefix, suffix='.xcf')
            os.close(fn[0])
            backupFiles[id] = fn[1]
        for id in delIDs:
            filename = backupFiles[id]
            del(backupFiles[id])
            try:
                os.remove(filename)
            except:
                print("ERROR: %s" % sys.exc_info()[0])
        for id, filename in backupFiles.items():
            img = curImages[id]
            try:
                print("saving %s-%s to %s"  % img.name, str(id), filename)
                pdb.gimp_xcf_save(1, img, img.active_drawable, filename, filename)
            except:
                print("ERROR: %s" % sys.exc_info()[0])
register(
    "autosave",
    "Autosave dirty hack",
    "Periodically saves all opened images to a temp directory",
    "public domain",
    "public domain",
    "2016",
    "<Image>/File/Activate Autosave",
    "*",
    [],
    [],
    autosave)
main()
