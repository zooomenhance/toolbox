import csv
import arcpy
import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob
import shutil
from shutil import copyfile

arcpy.CheckOutExtension("3D")
f = open('list.csv')
csv = csv.reader(f)
count = 0
for row in csv:
    count = count + 1
    print count
    print row[0]
    fileName = str(row[0])
    inCopy = "I:/APS2008Resource/" + fileName + ".aux.xml"
    outCopy = "I:/APS2008Resource/blockfiles/uncompress/working/"+ fileName + ".aux.xml"
    print fileName
    print inCopy
    print outCopy
    copyfile(inCopy, outCopy)
##    domain = tifFile[:-4] + '_domain.shp'
##    bufferDomain =  tifFile[:-4] + '_buffer.shp'
##    clip =  tifFile[:-4] + '_clip.tif'
##    print 'working on domain'
##    arcpy.RasterDomain_3d(tifFile, domain, "POLYGON")
##    print 'working on buffer'
##    arcpy.Buffer_analysis(domain, bufferDomain, "-300 Meters", "FULL", "ROUND", "NONE", "")
##    print 'working on clip'
##    desc = arcpy.Describe(bufferDomain)
##    ExtObj = desc.extent
##    clipExtent = "%d %d %d %d" % (ExtObj.XMin, ExtObj.YMin, ExtObj.XMax, ExtObj.YMax)
##    arcpy.Clip_management(tifFile, clipExtent, clip, bufferDomain, "256", "ClippingGeometry")
##    arcpy.Delete_management(domain)
##    arcpy.Delete_management(bufferDomain)
    print 'Finished working on' + fileName
print "Finished copying all .tif files"
