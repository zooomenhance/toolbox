import os
import arcgisscripting, os    
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob





####DOES NOT WORK!!



# Directory containing .las files
folder = "I:\\APS2008Resource\\blockfiles\\scripts\\extentTest\\test"
filepath = "I:\\APS2008Resource\\blockfiles\\scripts\\extentTest\\test"
# Name of extent file you are creating (full location)
extFile = "I:\\APS2008Resource\\2017_02_21_extentList.txt"

# Initialize list of .tif files and count of files
tif_files = []
##count = 0

### Go through folder, find all .tif files and add to list
##for filename in os.listdir(folder):
##    if filename.endswith(".tif"):
##        tif_files.append(filename)
##        count = count + 1

#print(las_files)
ascList = glob.glob(filepath + "/*.tif")  
print ascList  
       
##print('Number of .tif files: {}'.format(count))

# Open .txt file to write extent data for each .tif file
#with open(extFile, 'w') as f:
for ascFile in ascList:
    print ascFile
    print arcgisscripting.Raster(ascFile).extent
    myExtent = arcgisscripting.Raster(ascFile).extent
    newXMin = myExtent.XMin + 300
    newYMin = myExtent.YMin + 300
    newXMax = myExtent.XMax - 300
    newYMax = myExtent.YMax - 300
    newExtent = newXMin + " " + newYMin + " " + newXMax + " " + newYMax
    print newExtent
    in_raster = ascFile
    out_feature = "clip_" + ascFile
    arcpy.Clip_management(ascFile, newExtent, out_feature)
        ##extent1 = str(arcgisscripting.Raster(ascFile).extent)
        ##line = ascFile + " " + extent1 + '\n'
        ##f.write(line)

print('File written to\n {}'.format(extFile))
print('Closed: {}'.format(f.closed))
