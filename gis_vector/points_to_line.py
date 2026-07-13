# Batch process multiple ASCII to Raster files
# Method from: https://geonet.esri.com/thread/46801
# See bottom of page, comment by user "madanksuwal" (15 Mar 2013).

# Import system modules  
import arcgisscripting, os  
  
# Create the Geoprocessor object  
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob  
  
# Path to ascii files
filepath = r"E:/downloads/kayplaza/shp"
# Path where to put rasters  
outFolder = r"E:/downloads/kayplaza/shp/line"
  
ascList = glob.glob(filepath + "/*.shp")  
print ascList  
  
for ascFile in ascList:  
    outRaster = outFolder + "/" + os.path.split(ascFile)[1][:-4] + "_line"
    print outRaster  
    arcpy.PointsToLine_management(ascFile, outRaster)  
