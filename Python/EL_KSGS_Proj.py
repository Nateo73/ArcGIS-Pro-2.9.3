# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-03-09 13:17:26
This script is desinged to creat a set of elevation layers to add to a map for analsyis. 
"""
from ast import Try
from symbol import try_stmt
import arcpy,os,sys,time
from sys import argv
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map - Kansas Default*")[0]
#in_layer = aprxMap.listLayers("Clip_*")[0]
#In_Layer = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Projects\KS_Test_Geodatabase.gdb\Focal_Clip"
groupLayer = aprxMap.listLayers("elevation_group_layer")


flowSymbologyLayer = r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\AOI_FlowAcc.lyr"
elevation_group_layer = arcpy.mp.LayerFile (r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Elevation Products.lyrx")
def Model1(Input_Elevation_Layer, Flow_Direction_4=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Flow_Direction",
           Flow_Accumulation_8=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Flow_Accumulation",
           Contour_2ft_V=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Contour_2ft_V",
           Slope_2_=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Slope",
           Slope_4_=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Slope_3_"):
    # Flow Accumulation

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("3D")


    # Process: Fill (Fill) (sa)
    try:
        
        Output_surface_raster = ""
        Fill = Output_surface_raster
        Output_surface_raster = arcpy.sa.Fill(in_surface_raster=Input_Elevation_Layer, z_limit=None)
        Output_surface_raster.save(Fill)
        arcpy.AddMessage("Fill ran correctly. ")
    except:
        arcpy.AddMessage("")

    # Process: Flow Direction (Flow Direction) (sa)
    try:
        Flow_Direction = Flow_Direction_4
        Output_drop_raster = ""
        Flow_Direction_4 = arcpy.sa.FlowDirection(in_surface_raster=Output_surface_raster, force_flow="FORCE", out_drop_raster=Output_drop_raster, flow_direction_type="D8")
        Flow_Direction_4.save(Flow_Direction)
        arcpy.AddMessage(" Flow ran correctly. ")
    except:
        arcpy.AddMessage(" Flow did not run. ")

    # Process: Flow Accumulation (Flow Accumulation) (sa)
    try:
        Flow_Accumulation = Flow_Accumulation_8
        Flow_Accumulation_8 = arcpy.sa.FlowAccumulation(in_flow_direction_raster=Flow_Direction_4, in_weight_raster="", data_type="FLOAT", flow_direction_type="D8")
        Flow_Accumulation_8.save(Flow_Accumulation)
        arcpy.AddMessage(" Flow Accumulation ran correctly. ")
    except:
        arcpy.AddMessage(" Flow Accumulation did not run. ")


    # Process: Contour (Contour) (sa)
    #arcpy.sa.Contour(in_raster=Input_Elevation_Layer, out_polyline_features=Contour_2ft_V, contour_interval=2, base_contour=0, z_factor=1, contour_type="CONTOUR", max_vertices_per_feature=None)
    


    # Process: Slope (Slope) (sa)
    try:
        Slope = Slope_2_
        Slope_2_ = arcpy.sa.Slope(in_raster=Input_Elevation_Layer, output_measurement="PERCENT_RISE", z_factor=1, method="PLANAR", z_unit="FOOT_US")
        Slope_2_.save(Slope)
        Slope_3_ = Slope_4_
        Slope_4_ = arcpy.sa.Slope(in_raster=Input_Elevation_Layer, output_measurement="PERCENT_RISE", z_factor=1, method="PLANAR", z_unit="FOOT_US")
        Slope_4_.save(Slope_3_)
        arcpy.AddMessage("Slope ran correctly. ")
    except:
        arcpy.AddMessage("Slope did not run. " )



    # Process: Basin (Basin) (sa)
    """Output_raster = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Test_Geodabase.gdb\Basin_Flow_D2"
    Basin = Output_raster
    Output_raster = arcpy.sa.Basin(in_flow_direction_raster=Flow_Direction_4)
    Output_raster.save(Basin)"""


    # Process: Raster to Polygon (Raster to Polygon) (conversion)
    """arcpy.conversion.RasterToPolygon(in_raster=Output_raster, out_polygon_features=Output_polygon_features, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)"""
    
def createAttributeTable():
    try:
        in_int_Layer = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Flow_Accumulation"
        in_int_slope_S = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope"
        in_int_slope_G = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_3_"
        out_int_slope_S = arcpy.ia.Int(in_int_slope_S)
        out_int_slope_G = arcpy.ia.Int(in_int_slope_G)
        out_int_layer = arcpy.ia.Int(in_int_Layer)
        out_int_layer.save(r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Flow_Accumulation_int")
        out_int_slope_S.save(r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_s_int")
        out_int_slope_G.save(r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_g_int")
        
        in_layer_at = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Flow_Accumulation_int"
        in_slope_s_at = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_s_int"
        in_slope_g_at = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_g_int"
        
        
        
        
        arcpy.management.BuildRasterAttributeTable(in_layer_at, "Overwrite")
        arcpy.management.BuildRasterAttributeTable(in_slope_s_at, "Overwrite")
        arcpy.management.BuildRasterAttributeTable(in_slope_g_at, "Overwrite")
        
        arcpy.AddMessage("Attribute table created for Raster Layers")
    except:
        arcpy.AddWarning("Attribute table not created")
    
def createAcre():
    try:
        in_Layer = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Flow_Accumulation_int"
        slope_s_layer = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_s_int"
        slope_g_layer = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Geodatabases/KS_Elevation.gdb/Slope_g_int"
        add_fields =[["Acres","FLOAT","Acres"]]
        add_slope_field =[["Slope","LONG","Slope"]]
        slope_expression = "Value","$Feature.Slope"
        expression = "Round($feature.Value*.000247105,2)"
        arcpy.management.AddFields(slope_s_layer,add_slope_field)
        arcpy.management.AddFields(slope_g_layer,add_slope_field)
        arcpy.management.AddFields(in_Layer,add_fields)
        arcpy.CalculateField_management(in_Layer,"Acres", expression,"ARCADE")
        arcpy.CalculateField_management(slope_s_layer,"Slope","$Feature.Value" ,"ARCADE")
        arcpy.CalculateField_management(slope_g_layer,"Slope","$Feature.Value" ,"ARCADE")
        arcpy.AddMessage("Fields added")
        
        
        
        
        
        
        
        
    except:
        arcpy.AddWarning("Fields not added. ")

    
def addLayersToGroup():
    import arcpy,os,sys
    try:

        aprx = arcpy.mp.ArcGISProject('CURRENT')
        m = aprx.listMaps('Map - Kansas Default*')[0]
        outputWorkspace = r'C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers'
        arcpy.env.workspace = outputWorkspace
        slope_fc_output = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Slope_s_int"
        slope_fl_output = "SlopeSoils"
        slopeg_fc_output = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Slope_g_int"
        slopeg_fl_output = "SlopeGrazing"
        flow_acc_fc_output = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Flow_Accumulation_int"
        flow_acc_fl_output = "Flow Accumulation"
        contour_fc_output=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Contour_2ft_V"
        contour_fl_output="Contour_2ft_V"
        hillshade_fc_output =r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Hillshade"
        hillshade_fl_output = "Hillshade"
        blank_group_layer = arcpy.mp.LayerFile(r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Elevation Products.lyrx")
        flow_dir_output = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Flow_Direction"
        flow_dir_fl_output = "Flow Direction"
        m.addLayer(blank_group_layer, "TOP")
        model_output_group = m.listLayers("Elevation Products")[0]
        slope_fl_output = arcpy.MakeRasterLayer_management(slope_fc_output,slope_fl_output).getOutput(0)
        slopeg_fl_output = arcpy.MakeRasterLayer_management(slopeg_fc_output,slopeg_fl_output).getOutput(0)
        flow_acc_fl_output = arcpy.MakeRasterLayer_management(flow_acc_fc_output,flow_acc_fl_output).getOutput(0)
        contour_fl_output = arcpy.MakeFeatureLayer_management(contour_fc_output,contour_fl_output).getOutput(0)
        hillshade_fl_output = arcpy.MakeRasterLayer_management(hillshade_fc_output,hillshade_fl_output).getOutput(0)
        flow_dir_fl_output = arcpy.MakeRasterLayer_management(flow_dir_output,flow_dir_fl_output).getOutput(0)
        m.addLayerToGroup(model_output_group, slope_fl_output, "TOP")
        m.addLayerToGroup(model_output_group, slopeg_fl_output, "TOP")
        m.addLayerToGroup(model_output_group,flow_acc_fl_output, "TOP")
        m.addLayerToGroup(model_output_group,contour_fl_output, "BOTTOM")
        m.addLayerToGroup(model_output_group,hillshade_fl_output,"BOTTOM")
        m.addLayerToGroup(model_output_group,flow_dir_fl_output,"BOTTOM")
        arcpy.AddMessage(" Add Layers ran correctly. ")
    except:
        arcpy.AddMessage(" Add layers did not run correctly. ")
   
    
    
    
def symbolizeLayers():
    import arcpy,os,sys

    aprx = arcpy.mp.ArcGISProject("CURRENT")
    
    in_symbology_layer=r"C:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\Layers\Flow_Accumulation.lyrx"

   

    aprxMap = aprx.activeMap 

    
    in_layer = aprxMap.listLayers()[0]
    arcpy.AddMessage(in_layer)
    arcpy.AddMessage(in_symbology_layer)
    arcpy.AddMessage(in_symbology_layer)
    
def moveClipElevation():
    try:
        clipElevationProject = aprxMap.listLayers("Clip_elevation_project*")[0]
        fd=aprxMap.listLayers("Flow Direction*")[0]
        aprxMap.moveLayer(fd,clipElevationProject,"AFTER")
        arcpy.AddMessage("Clip Layer Moved")
    except:
        arcpy.AddMessage("Clip Layer not moved")
        

    
    
if __name__ == '__main__':
    with arcpy.EnvManager(scratchWorkspace=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb",
                          workspace=r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb"):
        
        in_layer = arcpy.GetParameterAsText(0)
        
        #Model1(*argv[1:])
        Model1(in_layer)
        createAttributeTable()
        createAcre()
        time.sleep(10)
        addLayersToGroup()
        moveClipElevation()
        exit()
        
        #symbolizeLayers()











        
