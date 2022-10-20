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
arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb"

def ScriptTool():
    



    try:
        targetFeatureList = arcpy.ListFeatureClasses()[0]
        exportFeatureClass = os.path.join(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb",targetFeatureList)
        exportXMLFile = os.path.join(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Export_Files",targetFeatureList +".xml")
        arcpy.management.ExportXMLWorkspaceDocument(exportFeatureClass,exportXMLFile,"DATA","BINARY","METADATA")
    except:
        arcpy.AddMessage("Feature Class not Present")


    return


if __name__ == '__main__':
    # ScriptTool parameters

    
    ScriptTool()

