import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob
import csv
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

# Directory containing .tif files
filepath = "I:\\APS2008Resource\\blockfiles\\scripts\\extentTest\\test"
##tifList = glob.glob(filepath + "/*.tif")
##tifCounter = len(glob.glob(filepath + "/*.tif"))
##print tifList
##print tifCounter
count = 0
f = open('rmapList.csv')
csv = csv.reader(f)
for row in csv:
    print row[0]
    row1 = str(row[0])
    tifFile = arcpy.sa.Raster(row1)
    print "working on " + tifFile
    count = count + 1
    print count
    extent = tifFile.extent
    XMin = extent.XMin
    if XMin > 0:
        domain = tifFile[:-4] + '_domain.shp'
        bufferDomain =  tifFile[:-4] + '_buffer.shp'
        clip =  tifFile[:-4] + '_clip.tif'
        print 'working on domain'
        arcpy.RasterDomain_3d(tifFile, domain, "POLYGON")
        print 'working on buffer'
        arcpy.Buffer_analysis(domain, bufferDomain, "-300 Meters", "FULL", "ROUND", "NONE", "")
        print 'working on clip'
        desc = arcpy.Describe(bufferDomain)
        ExtObj = desc.extent
        clipExtent = "%d %d %d %d" % (ExtObj.XMin, ExtObj.YMin, ExtObj.XMax, ExtObj.YMax)
        arcpy.Clip_management(tifFile, clipExtent, clip, bufferDomain, "256", "ClippingGeometry")
        arcpy.Delete_management(domain)
        arcpy.Delete_management(bufferDomain)
        print 'Finished working on' + tifFile
    else:
        print "skipped " + tifFile
print "Finished clipping all .tif files"

