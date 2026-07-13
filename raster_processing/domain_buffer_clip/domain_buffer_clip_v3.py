import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob
arcpy.CheckOutExtension("3D")
# Directory containing .tif files
filepath = "I:\\APS2008Resource\\blockfiles\\scripts\\extentTest\\test"
tifList = glob.glob(filepath + "/*.tif")
tifCounter = len(glob.glob(filepath + "/*.tif"))
print tifList
count = 0
for tifFile in tifList:
    print tifFile
    count = count + 1
    print count
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
print "Finished clipping all .tif files"

