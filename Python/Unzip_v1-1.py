import sys, zipfile, arcpy, os, traceback, datetime, time
from zipfile import ZipFile

#receive parameter from tool
infile = arcpy.GetParameterAsText(0)

#create timestamped folder to receive files from zip archive
fname = os.path.basename(infile).split('.')[0]
parentdir = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Export_Files"
renametime = time.ctime()
renameend = renametime.replace(" ","")
renamenocolon = renameend.replace(":","")
outdir = os.path.join(parentdir,"unzip" + fname + renamenocolon)

#unzip to created folder
with ZipFile(infile, 'r') as zipObj:
   zipObj.extractall(outdir)
   arcpy.AddMessage("Files extracted to: " + outdir) 
