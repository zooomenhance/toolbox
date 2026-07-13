import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
boundPoly = "//166.2.126.25/R2_VegMaps/Nebraska/Mapping/Riparian/riparian_mask_poly_smooth_dissolve2.shp"
arcpy.env.workspace = "//166.2.126.25/R2_VegMaps/Nebraska/Data/Imagery/Clipped_Imagery"
arcpy.env.snapRaster = "//166.2.126.25/R2_VegMaps/Nebraska/Mapping/Riparian/ValleyBottomPredict2.R.img"
arcpy.env.overwriteOutput=True
arcpy.env.nodata = "MINIMUM"


rasts = arcpy.ListRasters("*_s16.img")
##arcpy.ListFeatureClasses({wild_card}, {feature_type}, {feature_dataset})
print rasts
for rast in rasts:
    rastFileName = os.path.splitext(rast)[0]
    clipOutFile = rastFileName + "_clip.tif"
    Clip = ExtractByMask(arcpy.env.workspace + "\\" + rast, boundPoly)
    outClip = Clip.save(arcpy.env.workspace + "\\" + clipOutFile)
    
   
    
