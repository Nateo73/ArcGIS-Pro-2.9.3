"""
Tool:               Apply Symbology Elevation Tools
Version:            ArcGIS Pro 2.8.3
Author:             Nathan Osborn
Usage:              This script adds symbology from layerfiles to curent layers in the map. 

"""
import arcpy,os,sys
flowSymbologyLayer = r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Flow_AccumulationAcre.lyrx"
slopeSymbologyLayer = r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Slope_Soils_s.lyrx"
contourSymbologyLayer=r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Contour_2ftWhite.lyrx"
slopeGrazeSymbologyLayer=r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Slope_Grazing_s.lyrx"

def ScriptTool(flow,slope,contour,basins):
    
    
    arcpy.ApplySymbologyFromLayer_management(parameter0, flowSymbologyLayer,None,"MAINTAIN")
    arcpy.management.ApplySymbologyFromLayer(parameter2,slopeSymbologyLayer,None,"MAINTAIN")
    arcpy.ApplySymbologyFromLayer_management(parameter4,contourSymbologyLayer,None,"MAINTAIN")
    arcpy.management.ApplySymbologyFromLayer(parameter6,slopeGrazeSymbologyLayer,None,"MAINTAIN")
    return


if __name__ == '__main__':
    
    parameter0 = arcpy.GetParameterAsText(0)
    arcpy.SetParameterAsText(1, parameter0)
    parameter2 = arcpy.GetParameterAsText(2)
    arcpy.SetParameterAsText(3, parameter2)
    parameter4 = arcpy.GetParameterAsText(4)
    arcpy.SetParameterAsText(5, parameter4)
    parameter6 = arcpy.GetParameterAsText(6)
    arcpy.SetParameterAsText(7, parameter6)
    
    
    ScriptTool(parameter0,parameter2,parameter4,parameter6)
    exit()
