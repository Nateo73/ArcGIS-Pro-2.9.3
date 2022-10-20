"""
Tool:  This script works with the Elevation Tools task
Version: 1.0 updated on 9/7/2022
Author: Nathan Osborn
Required Arguments: The arguments are drawn from the active map. 
Description: This tool processes and runs several functions on a Clipped raster.
"""
import arcpy,os,sys
from arcpy.sa import Hillshade
import time
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap=aprx.listMaps("Map - Kansas Default*")[0]


def project_ks_clip_layer():
    ks_North = ["20043","20013","20131","20023","20117","20153","20201","20039","20157","20137","20089","20147","20183","20005","20085","20029","20181","20149","20193","20161",
             "20027","20179","20065","20123","20163","20141","20103","20087","20143","20209","20177","20197","20061","20105","20199","20109","20041","20063","20195","20091",
             "20167","20051","20045","20169","20127","20053"]
    ks_South = ["20139","20121","20059","20111","20071","20203","20171","20101","20135","20165","20009","20115","20113","20017","20159","20031","20107","20003","20145","20075","20093",
                "20055","20083","20185","20073","20079","20155","20011","20015","20001","20047","20207","20069","20173","20057","20151","20133","20205","20187","20067","20081","20037","20095",
                "20097","20049","20035","20191","20119","20025","20007","20099","20125","20129","20021","20189","20175","20077","20033","20019"]
    try:
        in_layer =  aprxMap.listLayers("Lidar_ks*")[0]
        project_layer =  aprxMap.listLayers("Clip_ElevationDASC*")[0]
        vertwkid = 6360
        wkid = 3427
        out_Raster = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Clip_elevation_project"
        in_layer_str = str(in_layer)
        """countyFips = in_layer_str[-3:]
        STFIPS = "20" + countyFips
        vertwkid = 6360
        if STFIPS in ks_North:
            wkid = 3427
        elif STFIPS in ks_South:
            wkid = 3428
        else:
            arcpy.AddMessage ("Lidar layer does not occur in Kansas. ")"""
        sr =arcpy.SpatialReference(wkid,vertwkid)
        arcpy.ProjectRaster_management (project_layer,out_Raster,sr,"NEAREST")
        aprxMap.addDataFromPath(out_Raster)

        arcpy.AddMessage("Clipped Layer was reprojected. ")
   
    except:
        arcpy.AddWarning("Cliiped Elevation Layer was not reprojected. ")

        return


def move_elevation_layer_back():
    try:
        eleLayer=aprxMap.listLayers("Elevation DEM Lidar*")[0]
        Lidar=aprxMap.listLayers("Hillshade DEM*")[0]
        aprxMap.moveLayer(Lidar,eleLayer,"BEFORE")

        arcpy.AddMessage("Elevation Layer moved back into place.")
    except:
        arcpy.AddMessage("Elevation Layer not moved.")
        
        
        
def changenameBack():
    try:
        el_layer = "Elevation DEM LiDAR-DASC"
        #in_layer =  aprxMap.listLayers("Lidar_ks*")[0]
        #in_layer_str = str(in_layer)
        #countyFips = in_layer_str[-3:]
        elLyr = aprxMap.listLayers("ElevationDASC*")[0]
        elLyrstring = str(elLyr.name)
        elLyr.name = elLyr.name.replace(elLyrstring,el_layer)          
        arcpy.AddMessage("Elevation county renamed")
        start_time = time.time()
        elapsed_time = (time.time()-start_time)
        arcpy.AddMassage("seconds " + elapsed_time )

        
        
        
    except:
        arcpy.AddWarning("Elevation Layer not renamed.")

def runFocalStats():
    try:
        in_raster = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Clip_elevation_project"
        out_raster = arcpy.sa.FocalStatistics(in_raster, "Rectangle 3 3 CELL", "MEAN", "DATA", 90);
        out_raster.save(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Clip_elevation_FS")
        arcpy.AddMessage("Focal Statistics ran correctly. ")

    except:
        arcpy.AddMessage("Focal Statistics did not run. ")
    
def createHillshade():
    try:
        targetLayer = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Clip_elevation_FS"
        if arcpy.Exists(targetLayer):
            Hillshade = arcpy.sa.Hillshade(targetLayer, 315, 45, "NO_SHADOWS", 1)
            Hillshade.save(r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Hillshade")
        else:
            arcpy.AddMessage ("Clip Layer does not exsist")
        arcpy.AddMessage("Hillshade ran successfully! ") 
      
    except:
        arcpy.AddMessage("Hillshade did not run. ")
def createContours():
    
    try:
        in_raster = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Clip_elevation_FS"
        arcpy.sa.Contour(in_raster, r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Contour_2ft_V",
        2, 0, 1, "CONTOUR", None)
        arcpy.AddMessage("Contours compleated! ")

    except:
        arcpy.AddMessage("Contours not run. " )
def alterContourTable():
    try:
        parm0 = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Elevation.gdb\Contour_2ft_V"
        drop_fields = "Id"
        add_fields =[['Type','TEXT','Type',10]]
        arcpy.management.AddFields(parm0,add_fields)
        arcpy.DeleteField_management(parm0,drop_fields)
        arcpy.AddMessage("Contour table Fields changed successfully. ")

    except:
        arcpy.AddMessage("Contour table Fields not changed. ")
def removeOrginClip():
    try:
        clipLayer=aprxMap.listLayers("Clip_ElevationDASC*")[0]
        aprxMap.removeLayer(clipLayer)
        arcpy.AddMessage("Original Clipped layer removed. ")

    except:
        arcpy.AddMessage(" Clipped layer not removed.")
        
if __name__ == '__main__':

    project_ks_clip_layer()
    changenameBack()
    move_elevation_layer_back()
    runFocalStats()
    createHillshade()
    createContours()
    alterContourTable()
    removeOrginClip()
    
    exit()
    

