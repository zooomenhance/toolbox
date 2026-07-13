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
filepath = r"C:\Users\adamclark\Downloads\drive-download-20170417T203500Z-001"
# Path where to put rasters  
outFolder = filepath
  
ascList = glob.glob(filepath + "/*.asc")  
print ascList  
  
for ascFile in ascList:  
    outRaster = outFolder + "/" + os.path.split(ascFile)[1][:-3] + "img"  
    print outRaster  
    arcpy.ASCIIToRaster_conversion(ascFile, outRaster, "FLOAT")  
