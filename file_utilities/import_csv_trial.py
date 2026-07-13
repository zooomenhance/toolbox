import csv
import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob

f = open('rmapList.csv')
csv_f = csv.reader(f)
##print csv_f
##filepath = "I:\\APS2008Resource\\blockfiles\\scripts\\extentTest\\test"
##tifList = glob.glob(filepath + "/*.tif")
##for tifFile in tifList:
##    print tifFile
##    print type(tifFile)
count = 0
for row in csv_f:
    print row[0]
##    print type(row)
##    row = str(row)
##    print row[
##    print type(row)
    row1 = str(row[0])
##    print type(row1)
    tifFile = arcpy.sa.Raster(row1)
##    print type(tifFile)
##    print tifFile.extent
    extent = tifFile.extent
##    print extent
    XMin = extent.XMin
##    print XMin
    if XMin > 0:
        countyes = count + 1
    else:
        countno = count +1
print  countyes
print  countno
