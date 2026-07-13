import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob
import time
arcpy.CheckOutExtension("3D")
# Directory containing .tif files
filepath = "O:\\Kaibab_NF\\Drive1"
tifList = glob.glob(filepath + "/*.tif")
print tifList
count = 0
for tifFile in tifList:
    total_start = time.clock()
    start = time.clock()
    print tifFile
    count = count + 1
    print count
    domainFile = 'G:\\RMAP_2017\\Kaibab_NF\\getflightlines' + tifFile[19:]
    domain = domainFile[:-4] + '_domain.shp'
##    bufferDomain =  tifFile[:-4] + '_buffer.shp'
##    clip =  tifFile[:-4] + '_clip.tif'
    print 'working on' + domain
    arcpy.RasterDomain_3d(tifFile, domain, "POLYGON")
##    print 'working on buffer'
##    arcpy.Buffer_analysis(domain, bufferDomain, "-300 Meters", "FULL", "ROUND", "NONE", "")
##    print 'working on clip'
##    desc = arcpy.Describe(bufferDomain)
##    ExtObj = desc.extent
##    clipExtent = "%d %d %d %d" % (ExtObj.XMin, ExtObj.YMin, ExtObj.XMax, ExtObj.YMax)
##    arcpy.Clip_management(tifFile, clipExtent, clip, bufferDomain, "256", "ClippingGeometry")
##    arcpy.Delete_management(domain)
##    arcpy.Delete_management(bufferDomain)
    print 'Finished working on ' + domain
    end = time.clock()
    total_end = time.clock()
    print("Total time %.3f" % (total_end - total_start))
print "Finished working on all .tif files"

