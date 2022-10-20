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
import pandas as pd


def xlstocsv():
    path = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Export_Files/TINPoints.xls"
    pathcsv = r"C:/geodata/project_data/nrcs/ArcGIS_Pro/Export_Files/TINPoints.csv"
    df = pd.read_excel(path)
    df.pop("OID")
    df.pop("Node_Index")
    col = df.pop("Elevation")
    df.insert(2,col.name,col)
    df.to_csv(pathcsv,header=False,index=False)

   

    return


if __name__ == '__main__':
    # ScriptTool parameters

    
    xlstocsv()

