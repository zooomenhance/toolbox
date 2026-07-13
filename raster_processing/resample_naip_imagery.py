import arcpy, os

## Processing variables - EDIT THESE
workspace = r"J:\Coconino_NF" #where all the quarter quads are stored 

#new folder to put the ouptput resampled images into
resampleFolder = workspace + "/resample_z12" 
if not os.path.isdir(resampleFolder):
	os.makedirs(resampleFolder)

#Dummy raster
Dummyrast = arcpy.sa.Raster(r'H:\R3\Coconino\coc_dummy_3m.img') #create this and make sure bigger than extent
##Dummyrast = arcpy.sa.Raster(r'K:\San_Juan\Data\Imagery\NAIP\SJNF_dummyRaster.img') #create this and make sure bigger than extent

zone = 12

# Project area to limit unneccessary processing 
##ProjectArea = r'K:\San_Juan\Data\Boundary\SanJuan_NF_Alps_boundary_utmzone13_2milebuffer.shp'
ProjectArea = r'H:\R3\Coconino\coc_dummy.shp'


# Specify factor 
DegradeFactor = 10

# Scale - output resolution
scale = 3

## Arcpy setup
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
arcpy.env.pyramid = "NONE"

####################################################################################################
##
##
## PROCESSING 
##
##
####################################################################################################

## Get reference extents
ext1 = Dummyrast.extent
xminS = ext1.XMin
xmaxS = ext1.XMax
yminS = ext1.YMin
ymaxS = ext1.YMax

extA = arcpy.Describe(ProjectArea).extent
xminA = extA.XMin
xmaxA = extA.XMax
yminA = extA.YMin
ymaxA = extA.YMax

#Get list of images
allRasters = arcpy.ListRasters("*.tif")
print (allRasters)
rastersZone = []
for rast in allRasters:
        ##if rast.split('_')[3]== str(zone):
        rastersZone.append(rast)
        ##else:
        ##        print rast, 'is not in this zone'

print ('checking...')
for rast in rastersZone:
        print(rast)
                

#Loop through each raster and aggregate and save to resampleFolder
for rast in rastersZone:
	#Get output Names
	rastName = rast.split(".")[0]
	print (rastName)
	clippedname = resampleFolder + "/" + rastName +"_clipped.tif"
	composite_name = resampleFolder + "/" + rastName +"_" + str(scale) + "m.img"
	integer_name = resampleFolder + "/" + rastName + "_" + str(scale) + "m_int8.img"
	
	
	#Get quarterquad raster extent
	quartquad = arcpy.sa.Raster(rast)
	ext2 = quartquad.extent
	xmin = ext2.XMin
	xmax = ext2.XMax
	ymin = ext2.YMin
	ymax = ext2.YMax
	
## Only process those rasters that intersect the study area
	if ((xmin >= xminA and xmin <= xmaxA) or (xmax >= xminA and xmax <= xmaxA)) and ((ymin >= yminA and ymin <= ymaxA) or (ymax >= yminA and ymax <= ymaxA)):
		print ('working on', rast)
		#Get a clean extent that will work nicely
		changed = False
		
		testXmin = (xmin - xminS)%scale
		if testXmin!=0:
			changed = True
			xmin = xmin+(scale-testXmin)
		testYmin = (ymin - yminS)%scale
		if testYmin!=0:
			changed = True
			ymin = ymin + (scale-testYmin)
		
		if changed:
			envelope = str(xmin) + " " + str(ymin) + " " + str(xmax) + " " + str(ymax)
			arcpy.Clip_management(rast,envelope,clippedname)
			#Aggregate each raster then combine
			layer1 = clippedname +"\Band_1"
			layer2 = clippedname +"\Band_2"
			layer3 = clippedname +"\Band_3"
			layer4 = clippedname +"\Band_4"
		else:
			layer1 = rast +"\Band_1"
			layer2 = rast +"\Band_2"
			layer3 = rast +"\Band_3"
			layer4 = rast +"\Band_4"
				
		
		
		
		
		ag1 = arcpy.sa.Aggregate(layer1,DegradeFactor,'MEAN','TRUNCATE','NODATA')
		ag1.save("tempag1.img")
		
		ag2 = arcpy.sa.Aggregate(layer2,DegradeFactor,'MEAN','TRUNCATE','NODATA')
		ag2.save("tempag2.img")
		
		ag3 = arcpy.sa.Aggregate(layer3,DegradeFactor,'MEAN','TRUNCATE','NODATA')
		ag3.save("tempag3.img")
		
		ag4 = arcpy.sa.Aggregate(layer4,DegradeFactor,'MEAN','TRUNCATE','NODATA')
		ag4.save("tempag4.img")
		
		
		arcpy.AddMessage("aggregation complete")
		arcpy.CompositeBands_management("tempag1.img;tempag2.img;tempag3.img;tempag4.img",composite_name)
		arcpy.CopyRaster_management(composite_name,integer_name,'','','','','','8_BIT_UNSIGNED')
		##take out trash
		arcpy.Delete_management("tempag1.img")
		arcpy.Delete_management("tempag2.img")
		arcpy.Delete_management("tempag3.img")
		arcpy.Delete_management("tempag4.img")
		arcpy.Delete_management(composite_name)
		if os.path.isfile(clippedname):
			arcpy.Delete_management(clippedname)
	else:
		print (rast, 'is not in your study area')

print ('done with all the rasters in:', workspace)










