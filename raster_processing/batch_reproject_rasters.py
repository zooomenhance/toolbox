import arcpy
import os

workspace = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\Reproject")
output = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\Reproject")

########### Option 1: Grab the spatial reference from another raster
#dataset = (r"\\166.2.126.25\R10_VegMaps\TongassNF\PrinceOfWales\Data\Imagery\!Mosaics\DOQ1m2006census.tif")
#spatial_ref = arcpy.Describe(dataset).spatialReference


########### Option 2: grab the spatial reference USING SYSTEM FACTORY CODE
#nad 1983 stateplane alaska 1 fips 5001 
spatial_ref = arcpy.SpatialReference()


#loop through all folders and files in the directory to find rasters
rasters = []
walk = arcpy.da.Walk(workspace, topdown=True, datatype= "RasterDataset")
for dirpath, dirnames, filenames in walk:
    #if "back_up" in dirnames:                        # Disregard any folder named 'back_up' in creating list of rasters
        #dirnames.remove('back_up')
    for filename in filenames:
        rasters.append(os.path.join(dirpath,filename))
        
#'print' ("Input rasters:")        
for raster in rasters: 
    print (raster)
    
print ("")
print "---------------------------------------------------------------"
print ("")


for raster in rasters:
    #split the raster name, create output name
    oName, oExt = os.path.splitext(raster)
    outName = os.path.join(output, oName + "_reproj.img")
    
    # Datum transfers require different parameters for ProjectRaster_management.
    # Must determine if the input raster has the same datum as the output projection datum
    sr = arcpy.Describe(raster).spatialReference
    datum = sr.GCS.datumName
    datum = datum[2:]   #for some reason "D_" is added to the beginning of the datum, and this is not accepted for the datum transform
    print datum         #so it has to be removed. Create a list "datums" to do this    
    
    #print "{}_To_NAD_1983".format(datum)
    
    print "working on {}".format(raster)

    #If datum name matches, then proceed. Adjust datum to match that of spatial_ref object
    if datum == "NAD_1983" or "North_American_1983":
            arcpy.ProjectRaster_management(raster, outName, 26931)
            print ("Finished " + raster)

    #If datum name doesn't match, than specify the geographic transform in the tool parameters. 
    elif datum != "NAD_1983" or "North_American_1983":
        arcpy.ProjectRaster_management(raster, outName, 26931,"","", "{}_To_NAD_1983".format(datum))
        print ("Finished " + raster)


print ("Operation Complete")
