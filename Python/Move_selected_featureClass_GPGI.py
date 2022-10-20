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


def ScriptTool(parameter0):
    arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb"
    try:
        featureClass = arcpy.GetParameterAsText(0)
        outputPath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb"
        outputName = "GPGI_Schema_MonY1"
        arcpy.conversion.FeatureClassToFeatureClass(featureClass,outputPath,outputName)
    except:
        arcpy.AddMessage("No Layers Present")
    

    return


if __name__ == '__main__':
    # ScriptTool parameters
    parameter0 = arcpy.GetParameterAsText(0)

    ScriptTool(parameter0)

