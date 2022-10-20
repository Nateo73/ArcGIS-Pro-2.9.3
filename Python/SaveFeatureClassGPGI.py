"""
Tool:               Save GPGI feature class to geodatabase
Version:            ArcGIS Pro 2.8.3
Author:             Nathan Osborn

"""
import arcpy


def ScriptTool():
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    aprxMap = aprx.listMaps("Map")[0]
    monitoringLayer=aprxMap.listLayers("GPGI_Schema_MonY1*")[0]
    if arcpy.Exists(monitoringLayer):
        arcpy.conversion.FeatureClassToGeodatabase(monitoringLayer, r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb")
    else:
        arcpy.AddMessage("Feature Class Not in Map")
        


    return


if __name__ == '__main__':


    
    ScriptTool()

