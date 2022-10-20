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
import arcpy,os,sys


def ScriptTool():
    arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb"        
    fl = arcpy.ListFeatureClasses()
    for f in fl:
        if arcpy.Exists(f):
            arcpy.management.Delete(f)

        else:
            arcpy.AddMessage("No feature classes Present")
    


    return


if __name__ == '__main__':

    
    ScriptTool()

