"""
Tool:               Add  GPGI Feature Class Schema to map
Source Name:        
Version:            ArcGIS Pro 2.8.3
Author:             Nathan Osborn
Usage:              
Required Arguments: None this will auto run to add the GPGI Feature Class Schema to the map 
Description:        This script will add the GPGI Feature Class Containing the GPGI Schema to the map so that features can be copied and pasted into this layer and be edited then copied and pasted back into the Portal GPGI Layer. 

"""
import arcpy,os,sys


def ScriptTool():
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    aprxMap = aprx.listMaps("Map")[0]
    aprxMap.addDataFromPath(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb\GPGI_Schema_MonY1")

    return


if __name__ == '__main__':

    
    ScriptTool()

