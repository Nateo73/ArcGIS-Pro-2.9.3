# Import system modules
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

# set environment settings
arcpy.env.workspace = outdir

# list of shapefiles in the output folder
fcList = arcpy.ListFeatureClasses()

# execute append for each input shapefile
for shapefile in fcList:
    desc = arcpy.da.Describe(shapefile)
    fields = arcpy.ListFields(shapefile)

    # for point geometry - confirm a CD field name and append to Local_Temp\Point
    if desc['shapeType'] == "Point":
        for field in fields:
            if field.name == 'pract_code':
                Point = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\Local_Temp.gdb\\Temporary\\Point"
                practicePoints_shp = shapefile
                arcpy.Append_management(practicePoints_shp, Point, "NO_TEST")
            else:
                arcpy.AddMessage("The input zip file <" + infile + "> does not contain a Conservation Desktop export.  Process terminated.")

    # for line geometry - confirm a CD field name and append to Local_Temp\Line    
    elif desc['shapeType'] == "Polyline":
        for field in fields:
            if field.name == 'pract_code':
                Line = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\Local_Temp.gdb\\Temporary\\Line"
                practiceLines_shp = shapefile
                arcpy.Append_management(practiceLines_shp, Line, "NO_TEST")
            else:
                arcpy.AddMessage("The input zip file <" + infile + "> does not contain a Conservation Desktop export.  Process terminated.")

    # for polygon geometry    
    elif desc['shapeType'] == "Polygon":
        
            for field in fields:
                # confirm a CD field name and append to Local_Temp\LandUnits
                if field.name == 'geom_stat':
                    LandUnit = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\Local_Temp.gdb\\Temporary\\LandUnits"
                    landUnits_shp = shapefile
                    arcpy.Append_management(landUnits_shp, LandUnit, "NO_TEST")

                # confirm a CD field name and append to Local_Temp\Polygon
                elif field.name == 'pract_code':
                    Polygon = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\Local_Temp.gdb\\Temporary\\Polygon"
                    practicePolygons_shp = shapefile
                    arcpy.Append_management(practicePolygons_shp, Polygon, "NO_TEST")

                else:
                    arcpy.AddMessage("The input zip file <" + infile + "> does not contain a Conservation Desktop export.  Process terminated.")

# cleanup
arcpy.Delete_management(outdir)

exit()
