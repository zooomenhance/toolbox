import csv
import os  
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
    inCopy = "H:/11-144_USFS_Wallow/Raw Image Scans/" + fileName
    outCopy = "H:/11-144_USFS_Wallow/RMAP/"+ fileName
    print fileName
    print inCopy
    print outCopy
    copyfile(inCopy, outCopy)
    print 'Finished working on' + fileName
print "Finished copying all .tif files"
