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
aprxMap=aprx.listMaps("Map*")[0]
AOILayer=aprxMap.listLayers("AdHoc Polygon*")[0]
outPath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb"
outName = "AOI"
inFC = os.path.join(outPath,"AOI")
def exportAOI():
    arcpy.conversion.FeatureClassToFeatureClass(AOILayer,outPath,outName)
    


    return
def addAOItomap():
    aprxMap.addDataFromPath(inFC)
    
    

if __name__ == '__main__':
    # ScriptTool parameters

    
    exportAOI()
    addAOItomap()

