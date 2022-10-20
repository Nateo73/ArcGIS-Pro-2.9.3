
import sys
import zipfile
import arcpy
import os
import traceback
import datetime
import time
from zipfile import ZipFile
rootdir = r'C:\geodata'
workFolder = r"C:\Users\Nathan.Osborn\Desktop"
renametime = time.ctime()
renameend = renametime.replace(" ", "")
renamenocolon = renameend.replace(":", "")
zipfileName = os.path.join(workFolder, renamenocolon + ".zip")
# create empty lists to receive files for zip archive
filesToWrite = []


def zipshapefile(rootdir):
    for rootdir, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            for file in files:
                # filter out .gdb files
                if not file.endswith('.gdb'):
                    filesToWrite.append(file)
                    # filesToDelete.append(file)
    with ZipFile(zipfileName, 'w', zipfile.ZIP_DEFLATED) as zipobj:
        for f in filesToWrite:
            zipobj.write(rootdir + "\\" + f, arcname=f)
    return


zipshapefile(rootdir)
