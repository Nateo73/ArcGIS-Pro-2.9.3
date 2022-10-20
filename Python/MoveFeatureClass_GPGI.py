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
    
    arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb"
    arcpy.env.overwriteOutput = True
    try:
        featureClass = arcpy.ListFeatureClasses()[0]
        outputPath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb"
        outputName = featureClass
        arcpy.conversion.FeatureClassToFeatureClass(featureClass,outputPath,outputName)
    except:
        arcpy.AddMessage("No Layers Present")


    return


if __name__ == '__main__':

    
    ScriptTool()

