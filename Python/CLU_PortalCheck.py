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

import arcpy,os

aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map - Kansas*")[0]
aprxLayer = aprxMap.listLayers()


def portalCheck():
    acportal = arcpy.GetActivePortalURL()
    scPortal = 'https://gis.sc.egov.usda.gov/portal/'

    if acportal != scPortal:
        #arcpy.SelectLayerByAttribute_management(in_layer,"NEW_SELECTION","tr = 'T0-R0'", None)
        arcpy.AddError("Please change your active portal to https://gis.sc.egov.usda.gov/portal/")
    else:
        arcpy.AddMessage("You are logged into the correct portal you may proceed")
        

    return
def cleargdb ():
    try:
        arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_scripting_ws.gdb"
        featureList = arcpy.ListFeatureClasses()
        rasterList = arcpy.ListRasters()
        fl=featureList + rasterList
        for f in fl:
            if arcpy.Exists(f):
                arcpy.management.Delete(f)
        arcpy.AddMessage("Geodatabase Cleared. ")
    except:
        arcpy.AddWarning("Geodatabase not Cleared ")
        
def moveLayer():
    try:
        sections=aprxMap.listLayers("Sections_a_ks*")[0]
        LocalTemp=aprxMap.listLayers("Local Temp*")[0]
        aprxMap.moveLayer(LocalTemp,sections,"AFTER")
        arcpy.AddMessage("Sections layer moved")
    except:
        arcpy.AddWarning("Sections layer not moved")       
        
        
    

if __name__ == '__main__':

    portalCheck()
    cleargdb()
    moveLayer()

    


