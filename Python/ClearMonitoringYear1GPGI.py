"""
Tool:               Clear Mointoring year 1 GPGI
Version:            ArcGIS Pro 2.8.3
Author:             Nathan Osborn
"""
import arcpy


def cleargdb():
        import arcpy
        import os
        arcpy.env.workspace = r"C:\geodata\project_data\nrcs\ArcGIS_Pro\Geodatabases\KS_Default_GPGI_MonY1.gdb"
        featureList = arcpy.ListFeatureClasses()
        rasterList = arcpy.ListRasters()
        fl=featureList + rasterList
        for f in fl:
            if arcpy.Exists(f):
                arcpy.management.Delete(f)
        return


if __name__ == '__main__':
    

    cleargdb()

