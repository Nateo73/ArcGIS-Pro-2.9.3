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


def ScriptTool():
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    aprxMap = aprx.listMaps("Map")[0]
    try:
        fc = aprxMap.listLayers("GPGI_Schema_MonY1")[0]
        for row in arcpy.SearchCursor(fc):
            fileName = row.case_name
            fileNameC = fileName.replace("-","_")
        fullPathName = os.path.join(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\GPGI_FGDB_KS.gdb\\",fileNameC)
        arcpy.management.Rename(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\GPGI_FGDB_KS.gdb\GPGI_Schema_MonY1",fullPathName,"FeatureClass")    
    except:
        print("Layer not present")
        arcpy.AddMessage("Layer not present")


    return


if __name__ == '__main__':

    
    ScriptTool()

