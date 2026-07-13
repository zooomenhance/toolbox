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
print tifList  
for tifFile in tifList:
    print tifFile
    ##domain = filepath + '\\' + tifFile[:-4] + '_domain.shp'
    domain = tifFile[:-4] + '_domain.shp'
    bufferDomain =  tifFile[:-4] + '_buffer.shp'
    clip =  tifFile[:-4] + '_clip.tif'
    print 'working'
    arcpy.RasterDomain_3d(tifFile, domain, "POLYGON")
    print domain
    arcpy.Buffer_analysis(domain, bufferDomain, "-300 Meters", "FULL", "ROUND", "NONE", "")
    print bufferDomain
    arcpy.Clip_management(tifFile, "#", clip, bufferDomain, "256", "ClippingGeometry")
    print clip
    arcpy.Delete_management(domain)
    arcpy.Delete_management(bufferDomain)
    print 'Finished working on' + tifFile

