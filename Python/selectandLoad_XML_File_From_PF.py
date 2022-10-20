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
    #arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Layers\programs"
    try:
        XMLFile = parameter0 = arcpy.GetParameterAsText(0)
        outpath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp.gdb"
        inpath = os.path.join(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Import_Files", XMLFile)
        arcpy.management.ImportXMLWorkspaceDocument(outpath,inpath,"DATA","")
    
    except:
        arcpy.AddMessage("No XML File Present")

    return


if __name__ == '__main__':
    # ScriptTool parameters
    parameter0 = arcpy.GetParameterAsText(0)

    
    ScriptTool(parameter0)

