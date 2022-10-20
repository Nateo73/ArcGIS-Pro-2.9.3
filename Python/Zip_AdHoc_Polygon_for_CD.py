import sys, zipfile, arcpy, os, traceback
from zipfile import ZipFile

# Allow overwriting outputs
arcpy.env.overwriteOutput = True

# Create temp folder
arcpy.management.CreateFolder(r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Export_Files", "shp_temp_polygon")

# Define variables
inFeatures = "Local Temp Layers\\AdHoc_Polygon"
outLocation = "C:\\geodata\\project_data\\nrcs\\tools\\ArcGIS_Pro_Utilities\\Export_Files\\shp_temp_polygon"
userInput = arcpy.GetParameterAsText(0)

# Validate userInput length
outNameLen = len(userInput)
if outNameLen>22:
    outName = userInput[0:21] + "_a"
else:
    outName = userInput + "_a"    

# Export AdHoc_Polygon to shapefile
arcpy.conversion.FeatureClassToFeatureClass(in_features=inFeatures, out_path=outLocation, out_name=outName + ".shp")

#receive path of shapefile to be zipped
shapefileName = os.path.join(outLocation, outName + ".shp")
#define target directory
workFolder = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Export_Files\Files_for_Import_to_CD"
#return input file name without extension
fname = os.path.basename(shapefileName).split('.')[0]
#folder where files to be zipped reside
fileloc = os.path.dirname(shapefileName)
#create list of files in folder
files = os.listdir(fileloc)
# define zip archive name
zipfileName = os.path.join(workFolder,fname +".zip")
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

    # Cleanup
    arcpy.Delete_management(outLocation)
exit()
