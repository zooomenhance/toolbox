import arcpy
from arcpy import env
from arcpy.sa import *
import glob
from shutil import copy2
import shutil
arcpy.CheckOutExtension('spatial')
env.workspace = r'H:\TEST\bird2017\big_year_2017_12_19\Big Year 2017\csv\test'
files = glob.glob(r'H:\TEST\bird2017\big_year_2017_12_19\Big Year 2017\csv\test\*.csv')
sr = arcpy.SpatialReference(4326)
print files
for file in files:
    #make sure we have the right files
    print file
    print file[:-4]
    #create variables
    output = file[:-4] + "_points"
    output_mbr = file[:-4] + "_mbr"
    output_lines = file[:-4] + "_lines"
    print output
    #print saved_output
    #create points from lat long and save as a layer file
    arcpy.MakeXYEventLayer_management(file, "lat_xstart", "long_ystart", output)
    arcpy.SaveToLayerFile_management(output, output)
    print file[-13:] + " points created"
    #find the minimum bounding rectangle of these points and save as a shapefile and then a layer file
    arcpy.MinimumBoundingGeometry_management (output, output_mbr, "ENVELOPE")
    arcpy.MakeFeatureLayer_management (output_mbr + ".shp", output_mbr)
    arcpy.SaveToLayerFile_management(output_mbr, output_mbr)
    print file[-13:] + " MBR created"
    #create line segments from each point and save as a shapefile and then as a layer file
    arcpy.XYToLine_management (file, output_lines, "lat_xstart", "long_ystart", "lat_xend", "long_yend", "GEODESIC", "fid", sr)
    arcpy.MakeFeatureLayer_management (output_lines + ".shp", output_lines)
    arcpy.SaveToLayerFile_management(output_lines, output_lines)
    print file[-13:] + " Lines created"
    ##convert to kml
    arcpy.LayerToKML_conversion (output + ".lyr", output + ".kmz")
    arcpy.LayerToKML_conversion (output_mbr + ".lyr", output_mbr + ".kmz")
    arcpy.LayerToKML_conversion (output_lines + ".lyr", output_lines + ".kmz")


