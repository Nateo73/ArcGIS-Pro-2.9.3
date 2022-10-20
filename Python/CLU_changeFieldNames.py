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
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap=aprx.listMaps("Map*")[0]
in_layer =  aprxMap.listLayers("CLU_ks*")[0]

fields = {'farm_number':'farm','tract_number':'tract','clu_number':'plu_number','highly_erodible_land_type_code':'hel','clu_number':'plu_number'}


drop_fields = ['clu_classification_code','clu_calculated_acreage','comments','data_source_site_identifier','state_code','county_code','creation_date','last_change_date','data_source','admin_state','admin_county','cropland_indicator_3CM','sap_crp','clu_status','cdist_fips','edit_reason','GlobalId','clu_alt_id','last_chg_user_nm','state_ansi_code','county_ansi_code','clu_identifier']
add_fields =[['plu_id','LONG','plu_id'],['case_id','LONG','case_id'],['status','TEXT','status'],['county','TEXT','county',254],['state','TEXT','state',254],['geom_stat','TEXT','geom_stat'],['plu_status','TEXT','plu_status',254],['case_name','TEXT','case_name',254],['plu_name','TEXT','plu_name',254],['land_use','TEXT','land_use',254],['land_use_m','TEXT','land_use_m',254],['calc_acres','DOUBLE','calc_acres'],['prog_acres','DOUBLE','prog_acres'],['ownership','TEXT','ownership',254],['last_chang','TEXT','last_chang',254],['nest_progr','TEXT','nest_progr',254],['nest_id','TEXT','nest_id',254],['c_locked','LONG','c_locked'],['can_delete','LONG','can_delete'],['has_area_p','LONG','has_area_p'],['plu_subfield','TEXT','plu_subfield']]

arcpy.management.AddFields(in_layer,add_fields)
arcpy.DeleteField_management(in_layer,drop_fields)











def ChangeFields():
    try:
        for key in fields:
           field = key
           newfield = fields[key]
           arcpy.AlterField_management(in_layer,field,newfield,newfield)
    except:
        arcpy.AddMessage("Fields do not exist")

    return


if __name__ == '__main__':
    ChangeFields()
 

