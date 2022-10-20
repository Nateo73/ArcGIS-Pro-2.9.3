# Selection of photo option for FSA/FACTA Compliance Review Reports
# For incorporation into ArcGIS Pro tasks
# Requires input parameter value list of "No Photos" and "Include Photos"
# Created May 2022 by Levi Gibson, Kansas NRCS
# Last update 9/12/2022

import arcpy
from sys import argv

# Allow overwriting outputs
arcpy.env.overwriteOutput = True

# Get the selected parameter
selection = arcpy.GetParameter(0)

# Process: Export Report
PDF_File = "C:\\geodata\\project_data\\nrcs\\ArcGIS_Pro\\Export_Files\\FSA_FACTA_Compliance_Report.pdf"
if selection == "No Photos":
    arcpy.management.ExportReportToPDF(in_report="FSA_FACTA Compliance Review Report_No Photos", out_pdf_file=PDF_File, expression="", resolution=96, image_quality="BEST", embed_font="EMBED_FONTS", compress_vector_graphics="COMPRESS_GRAPHICS", image_compression="ADAPTIVE")
elif selection == "Include Photos":
    arcpy.management.ExportReportToPDF(in_report="FSA_FACTA Compliance Review Report_With Photos", out_pdf_file=PDF_File, expression="", resolution=96, image_quality="BEST", embed_font="EMBED_FONTS", compress_vector_graphics="COMPRESS_GRAPHICS", image_compression="ADAPTIVE")
