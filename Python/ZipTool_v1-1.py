import sys, zipfile, arcpy, os, traceback, datetime, time
from zipfile import ZipFile

#receive path of shapefile to be zipped
parameter0 = arcpy.GetParameterAsText(0)
#define target directory
workFolder = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Export_Files"
#return input file name without extension
fname = os.path.basename(parameter0).split('.')[0]
#folder where files to be zipped reside
fileloc = os.path.dirname(parameter0)
#create list of files in folder
files = os.listdir(fileloc)
#timestamp and define zip archive name
renametime = time.ctime()
renameend = renametime.replace(" ","")
renamenocolon = renameend.replace(":","")
zipfileName = os.path.join(workFolder,fname + renamenocolon +".zip")
#create empty lists to receive files for zip archive
filesToWrite = []
#filesToDelete =[]

#search working directory for files of the same name and add them to the zip archive
def zipshapefile(fileloc):
    for file in files:
        if fname == file[0:-4]:
            #filter out .lock files
            if not file.endswith('.lock'):
                filesToWrite.append(file)
                #filesToDelete.append(file)
    with ZipFile(zipfileName,'w', zipfile.ZIP_DEFLATED) as zipobj:
        for f in filesToWrite:
            zipobj.write( fileloc + "\\" + f, arcname=f)
    return

#This function deletes files after they are added to the zip archive
#def deletefileszipped():
#    for ff in filesToDelete:
#        os.remove( fileloc + "\\" + ff)
#    return

#run the script
if __name__ == '__main__':
    zipshapefile(fileloc)
    #deletefileszipped()
    #display message showing location and names of files added to zip archive
    arcpy.AddMessage("Added:" + '\n' + '\n'.join(filesToWrite) + '\n' + "From: " + fileloc + '\n' + "To: " + zipfileName)
