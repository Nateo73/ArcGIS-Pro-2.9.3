# Soils Interp Reports Tool
# Intersects the Kansas temp.gdb-Land Units and Kansas statewide soil_interps_ks000 layer
# Exports results to an excel file and imports symbolized layers 
# Created September 2022 by Levi Gibson, Kansas NRCS
# Last update: 09/13/2022

import arcpy
import os

def SoilInterpAnalysis():  # Soil Interp Analysis

    # Allow overwriting outputs
    arcpy.env.overwriteOutput = True

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx")
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx")
    # Model Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\geodatabases\SoilsReports.gdb", workspace=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Projects\KS_NRCS_Default\SoilsReports.gdb"):
        Land_Units = "Local Temp Layers\\Land Units"
        soil_interps_ks000 = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\geodata.gdb\\Soils\\soil_interps_ks000"

        # Define project, map, and Soils Reports Layers        
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        aprxMap = aprx.listMaps("Map - Kansas Default*")[0]   

        # Add existing soil_interp_analysis feature class to map.  Required to avoid issues with caching in ArcGIS Pro
        aprxMap.addDataFromPath("C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\SoilsReports.gdb\\soil_interp_analysis")
        
        # Remove existing instance of Soils Reports Layers
        try:
            soilLyrOld = aprxMap.listLayers("Soils Reports Layers")[0]    
            aprxMap.removeLayer(soilLyrOld)
        except:
            pass
        try:
            soilMuOld = aprxMap.listLayers("Soil Map Unit Report")[0]
            aprxMap.removeLayer(soilMuOld)
        except:
            pass
        try:
            ecoSiteOld = aprxMap.listLayers("Ecological Site Report")[0]
            aprxMap.removeLayer(ecoSiteOld)
        except:
            pass

        # Process: Buffer input land units (10 ft)
        output_buffer = os.path.join("in_memory", "buffer")
        arcpy.analysis.Buffer(in_features=Land_Units, out_feature_class=output_buffer, buffer_distance_or_field="10 Feet", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="GEODESIC")

        # Process: Clip soil interp input with buffered land units
        output_clip = os.path.join("in_memory", "clip")
        arcpy.analysis.Clip(in_features=soil_interps_ks000, clip_features=output_buffer, out_feature_class=output_clip, cluster_tolerance="")

        # Process: Intersect land units and clipped soil interps
        soil_interp_analysis = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\geodatabases\\SoilsReports.gdb\\soil_interp_analysis"
        arcpy.analysis.Intersect(in_features=[[Land_Units, ""], [soil_interps_ks000, ""]], out_feature_class=soil_interp_analysis, join_attributes="NO_FID", cluster_tolerance="", output_type="INPUT")

        # Process: Add Field "soil_int_acres"
        soil_interp_analysis_2_ = arcpy.management.AddField(in_table=soil_interp_analysis, field_name="soil_int_acres", field_type="DOUBLE", field_precision=None, field_scale=None, field_length=None, field_alias="soil_int_acres", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")[0]

        # Process: Calculate Geometry Attributes for "soil_int_acres" field
        soil_interp_analysis_3_ = arcpy.management.CalculateGeometryAttributes(in_features=soil_interp_analysis_2_, geometry_property=[["soil_int_acres", "AREA_GEODESIC"]], length_unit="", area_unit="ACRES", coordinate_system="PROJCS[\"NAD_1983_UTM_Zone_14N\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-99.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", coordinate_format="SAME_AS_INPUT")[0]

        # Process: Table To Excel
        soils_interp_analysis_xlsx = "C:\\geodata\\project_data\\nrcs\\tools\\ArcGIS_Pro_Utilities\\Export_Files\\soils_interp_analysis.xlsx"
        arcpy.conversion.TableToExcel(Input_Table=soil_interp_analysis_3_, Output_Excel_File=soils_interp_analysis_xlsx, Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")

        # Add Soils Reports layer
        soilLyr = arcpy.mp.LayerFile(r"C:\\geodata\project_data\nrcs\ArcGIS_Pro\Layers\soils\SoilsReports.lyrx")
        aprxMap.addLayer(soilLyr)

        # Remove soil_interp_analysis feature class from map
        try:
            soilInterpFeature = aprxMap.listLayers("soil_interp_analysis")[0]    
            aprxMap.removeLayer(soilInterpFeature)
        except:
            pass
        
if __name__ == '__main__':
    SoilInterpAnalysis()
