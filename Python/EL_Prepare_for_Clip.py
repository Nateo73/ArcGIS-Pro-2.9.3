"""
Tool:               This script works with the Elevation Tools task
Author:            Nathan Osborn
Required Arguments: The arguments are drawn from the active map. 
Description: This tool prepares the map with the proper layers in the table of contents to run a Raster Function Clip in the elevation tools task.
Version 1.0 updated on 9/7/2022
"""
import arcpy,os,sys
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map - Kansas*")[0]
aprxLayer = aprxMap.listLayers()
arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb"
featureList = arcpy.ListFeatureClasses()
rasterList = arcpy.ListRasters()
fl=featureList + rasterList
def removeElevationProducts():
    try:
        for lyr in aprxLayer:
            if lyr.supports("NAME"):
                if lyr.name == "Elevation Products":
                    aprxMap.removeLayer(lyr)
        arcpy.AddMessage("Elevation Products Removed")
    except:
        arcpy.AddWarning("No Elevation Layer Present")


    return

def clearGDB():
    try:
        for f in fl:
            if arcpy.Exists(f):
                arcpy.management.Delete(f)
        arcpy.AddMessage("Elevation Geodatabase cleared")        
    except:
        arcpy.AddWarning("Elevation Geodatabase not cleared")

def replaceFC():
    try:
        elLyr = aprxMap.listLayers("Elevation_ks*")[0]
        elLyrstring = str(elLyr.name)
        elLyr.name = elLyr.name.replace(elLyrstring,"ElevationCounty")
        arcpy.AddMessage("Lidar Elevation Layer Renamed")
    except:
        arcpy.AddWarning("Lidar Elevation Layer not renamed")
                
def moveLayer():
    try:
        eleLayer=aprxMap.listLayers("Elevation_ks*")[0]
        height=aprxMap.listLayers("Administrative*")[0]
        aprxMap.moveLayer(height,eleLayer,"BEFORE")
        arcpy.AddMessage("Elevation County layer moved")
    except:
        arcpy.AddWarning("Elevation County layer not moved")


def checkElevationCounty():
    try:
        aprxLayer = aprxMap.listLayers("ElevationCounty*")
        total =len(aprxLayer)
        if total == 1:
            arcpy.AddMessage("Clip good to run")
        else:
            arcpy.AddError("Please remove all Elevation County layers and try again. ")

    except:
        arcpy.AddWarning("There are too many elevation layers present in the map.")
if __name__ == '__main__':

    
    removeElevationProducts()
    clearGDB()
    moveLayer()
    #checkElevationCounty()
    replaceFC()
    
    exit()
    

