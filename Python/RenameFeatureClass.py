"""
Tool:               <Tool label>
Source Name:        <File name>
Version:            <ArcGIS Version>
Author:             <Author>
Usage:              <Command syntax>
Required Arguments: <parameter0>
                    <parameter1>
Optional Arguments: <parameter2>
                    <parameter3>
Description:        <Description>
"""
import arcpy
import os
arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb"

try:
    featureList = arcpy.ListFeatureClasses("GPGI_Schema_MonY1")[0]
    if arcpy.Exists(featureList):
        for row in arcpy.SearchCursor(featureList):
            fileName = row.case_name
            fileNameC = "".join(c for c in fileName if c.isalnum())
        fullPathName = os.path.join(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb\\",fileNameC)
        arcpy.management.Rename(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb\GPGI_Schema_MonY1",fullPathName,"FeatureClass")   
    else:
        arcpy.AddMassage("Feature class not present")
except:
    arcpy.AddMessage("No such Layer")



