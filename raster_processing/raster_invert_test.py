import arcpy 
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')
arcpy.env.workspace=r'G:\RMAP_2017\Coronado_NF\2017_01_23_cleanup\combined\chm\home2'
#pathway to all rasters in workspace directory
rasters = arcpy.ListRasters('*_sps10k.img*')
for raster in rasters:
    print('start invert')
    outraster = Raster(raster) * -1
    print(raster)
    #Save temp raster to disk with new name
    outraster.save(raster[:-4] + "_inv.img")
    print('save invert')

print('Done Processing')

