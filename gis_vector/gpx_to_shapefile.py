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
filepath = r"E:/downloads/kayplaza"
# Path where to put rasters  
outFolder = r"E:/downloads/kayplaza/kayplaza.gdb"
  
ascList = glob.glob(filepath + "/*.gpx")  
print ascList  
  
for ascFile in ascList:  
    outRaster = outFolder + "/" + os.path.split(ascFile)[1][:-4]  
    print outRaster  
    arcpy.GPXtoFeatures_conversion(ascFile, outRaster)  
