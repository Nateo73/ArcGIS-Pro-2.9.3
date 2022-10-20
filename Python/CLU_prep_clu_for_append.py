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
import arcpy
try:
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    aprxMap=aprx.listMaps("Map - Kansas Default*")[0]
    in_layer =  aprxMap.listLayers("CLU_ks*")[0]
    appLayer = aprxMap.listLayers("Land Units*")[0]
    arcpy.AddMessage("Layers Found")
except:
    arcpy.AddWarning("Cannot find a CLU Layer")

def alterfields():
    try:
        arcpy.SetProgressor("Changing Field Names")
        field1 = 'highly_erodible_land_type_code'
        newfield1 = 'hel'
        nalias = "hel"
        new_type = "TEXT"
        new_length = 254
        new_is_nullable = "NULLABLE"

        field2 = "clu_number"
        nfield2 = "plu_number"
        nalias2 = "plu_number"

        field3 = "farm_number"
        nfield3 = "farm"
        nalias3 = "farm"
        nlength3 = 7




        arcpy.AlterField_management(in_layer,field1,newfield1,nalias,new_type,new_length,new_is_nullable)
        arcpy.AlterField_management(in_layer,field2,nfield2,nalias2,new_type,new_length,new_is_nullable)
        arcpy.AlterField_management(in_layer,field3,nfield3,nalias3,new_type,nlength3,new_is_nullable)
        
        arcpy.AddMessage("Success Fields Altered! ")
    except:
        arcpy.AddMessage("Alter Fields did not run correctly. ")
    return



def addRemoveFields():
    try:
        print("\tRemoving unwanted Fields. ")
        drop_fields = ['GlobalId','clu_classification_code','clu_calculated_acreage','comments','data_source_site_identifier','state_code','county_code','creation_date','last_change_date','data_source','admin_state','admin_county','cropland_indicator_3CM','sap_crp','clu_status','cdist_fips','edit_reason','clu_alt_id','last_chg_user_nm','state_ansi_code','county_ansi_code','clu_identifier']
        add_fields =[["tract","LONG","tract"], ['case_id','LONG','case_id'],['status','TEXT','status'],['county','TEXT','county',254],['state','TEXT','state',254],['geom_stat','TEXT','geom_stat',254],['plu_status','TEXT','plu_status',254],['case_name','TEXT','case_name',254],['plu_name','TEXT','plu_name',254],['land_use','TEXT','land_use',254],['land_use_m','TEXT','land_use_m',254],['calc_acres','DOUBLE','calc_acres'],['prog_acres','DOUBLE','prog_acres'],['ownership','TEXT','ownership',254],['last_chang','TEXT','last_chang',254],['nest_progr','TEXT','nest_progr',254],['nest_id','TEXT','nest_id',254],['c_locked','LONG','c_locked'],['can_delete','LONG','can_delete'],['has_area_p','LONG','has_area_p'],['plu_subfield','TEXT','plu_subfield',7],['plu_id','LONG','plu_id']]

        arcpy.management.AddFields(in_layer,add_fields)
        arcpy.DeleteField_management(in_layer,drop_fields)
        arcpy.CalculateField_management(in_layer,"tract","$feature.tract_number","ARCADE")
        arcpy.DeleteField_management(in_layer,"tract_number")
        arcpy.AddMessage("Unwanted fields removed. ")
    except:
        arcpy.AddMessage("Remove fields did not run correctly. ")
    return

def appendCLU():
    try:
        print("\tPasting features into Land Unit Layer. ")
        arcpy.Append_management(in_layer,appLayer,"TEST")
        arcpy.AddMessage("Features appended. ")
    except:
        arcpy.AddMessage("Append features did not run correctly. ")

def removeCLU():
    try:
        print("Removing CLU Layer")
        aprxMap.removeLayer(in_layer)
        arcpy.AddMessage("CLU layer removed. ")
    except:
        arcpy.AddMessage("Remove CLU Layer did not excute correctly .")

def addGlobalID():
    try:
        arcpy.management.AddGlobalIDs(in_layer)
        arcpy.AddMessage("Global IDs Added")
     
    except:
        arcpy.AddMessage("Add Global ID did not run")
def moveLayer():
    try:
        sections=aprxMap.listLayers("Sections_a_ks*")[0]
        moveto=aprxMap.listLayers("Township*")[0]
        lu = aprxMap.listLayers("Land Units")
        ap = aprxMap.listLayers("AdHoc_Polygon")
        aprxMap.moveLayer(moveto,sections,"AFTER")
        aprxMap.moveLayer(ap,lu,"AFTER")
        arcpy.AddMessage("Sections layer moved")
    except:
        arcpy.AddWarning("Sections layer not moved")  

if __name__ == '__main__':
    alterfields()
    addRemoveFields()
    addGlobalID()
    appendCLU()
    removeCLU()
    moveLayer()

