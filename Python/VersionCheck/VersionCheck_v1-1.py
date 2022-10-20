#Tool:               VersionCheck
#Source Name:        VersionCheck_v1-1.py
#Version:            ArcGIS Pro 2.8.3, Python 3.7.10
#Author:             Joel Thompson
#Usage:              On Kansas_Default project startup
#Description:        Checks current vs installed versions of ArcGIS Pro, geodata.gdb, Local_Temp.gdb

import sys, arcpy, os, traceback, datetime, time

def Protxtver():
    txtPropath = (r'F:\geodata\project_data\nrcs\tools\ArcGIS_Pro_Utilities\ArcGISPro_Version.txt')
    #check that version.txt file exists
    if os.path.exists(txtPropath):
        txtPro = open(txtPropath, 'r')
        line1 = txtPro.readline()
        # remove white spaces
        txtver = line1.strip()
        #return target Pro version
        return txtver
    else:
        #show error and exit code if txt file does not exist
        arcpy.AddError("ArcGISPro_Version.txt does not exist on server. Cannot confirm correct version of ArcGIS Pro is installed. Contact the technology team.")
        sys.exit("ArcGIS Pro installation missing required elements")
        
def GDBver():
    #check that geodatabase exists on workstation
    gdbpath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\geodatabases\geodata.gdb"
    if not os.path.exists(gdbpath):
            arcpy.AddError("geodata.gdb does not exist on C:. Please use Geodata tools to Update Workstation Tools")
            sys.exit("geodata.gdb missing from C:")
    #define location of table containing database version information
    fc = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\geodatabases\geodata.gdb\FGDB_version"
    # Use SearchCursor to access data in version column of gdbver table
    with arcpy.da.SearchCursor(fc, ['Version']) as cursor:
        for row in cursor:
            # Write first row of table's Version column to variable, end loop, and reset cursor
            ver = row[0]
            break
            del cursor
    #return current GDB version
    return ver

def GDBtxtver():
    txtGDBpath = (r'F:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Geodata_Version.txt')
    #check that version.txt file exists
    if os.path.exists(txtGDBpath):
        txtGDB = open(txtGDBpath, 'r')
        line1 = txtGDB.readline()
        # remove white spaces
        txtver = line1.strip()
        #return target GDB version
        return txtver
    else:
        arcpy.AddWarning("Geodata_Version.txt file does not exist on server. Contact the technology team.")

def tempGDBver():
    #check that geodatabase exists on workstation
    gdbpath = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\geodatabases\Local_Temp.gdb"
    if not os.path.exists(gdbpath):
            arcpy.AddError("Local_Temp.gdb does not exist on C: Please use Geodata tools to Update Workstation Tools")
            sys.exit("Local_Temp.gdb missing from C:")
    #define location of table containing database version information
    fc = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\geodatabases\Local_Temp.gdb\FGDB_version"
    # Use SearchCursor to access data in version column of gdbver table
    with arcpy.da.SearchCursor(fc, ['Version']) as cursor:
        for row in cursor:
            # Write first row of table's Version column to variable, end loop, and reset cursor
            ver = row[0]
            break
            del cursor
    #return current GDB version
    return ver      

def tempGDBtxtver():
    txtGDBpath = (r'F:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\Local_Temp_Version.txt')
    #check that version.txt file exists
    if os.path.exists(txtGDBpath):
        txtGDB = open(txtGDBpath, 'r')
        line1 = txtGDB.readline()
        # remove white spaces
        txtver = line1.strip()
        #return target GDB version
        return txtver
    else:
        arcpy.AddWarning("Local_Temp_Version.txt file does not exist on server. Contact the technology team.")

#assign currently installed and target version of ArcGIS Pro to variables
varPro_version = arcpy.GetInstallInfo()['Version']
varProtext_version = Protxtver()
#compare installed Pro version to target
if varPro_version != varProtext_version:
    #show error and exit code if installed and target version do not match
    arcpy.AddError("Incorrect version of ArcGIS Pro installed. Installed version: "
                   + varPro_version + " Correct version: " + varProtext_version +
                   " Contact CEC to assist with installation of the correct version.")
    sys.exit("ArcGIS Pro installation missing required elements")
    
#assign currently installed and target Geodatabase version to variables
varGDB_version = GDBver()
varGDBtext_version = GDBtxtver()
#compare installed version to target
if varGDB_version != varGDBtext_version:
    #show warning if most recent geodatabase version not in use
    arcpy.AddWarning("New version of geodata.gdb available. Installed version: "
                   + varGDB_version + " Correct version: " + varGDBtext_version +
                    " Next time you are in the USDA office please use Geodata tools to Update Workstation Tools")

#assign currently installed and target Local Temp Geodatabase version to variables
vartempGDB_version = tempGDBver()
vartempGDBtext_version = tempGDBtxtver()
#compare installed version to target
if vartempGDB_version != vartempGDBtext_version:
    #show warning if most recent geodatabase version not in use
    arcpy.AddWarning("New version of Local_Temp.gdb available. Installed version: "
                   + vartempGDB_version + " Correct version: " + vartempGDBtext_version +
                     " Next time you are in the USDA office please use Geodata tools to Update Workstation Tools")

arcpy.AddMessage("ArcGIS Pro and Geodatabase version check complete.")
