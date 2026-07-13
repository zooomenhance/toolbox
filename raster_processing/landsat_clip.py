import arcpy
dem = "\\166.2.126.227\International_Programs\Ethiopia\2017_01_20_mapupdate\topographic\borena_subarea_dem_wgs84_utmz37_30m.img"
demClip = "\\166.2.126.227\International_Programs\Ethiopia\2017_01_20_mapupdate\topographic\borena_subarea_dem_wgs84_utmz37_30m_clip.img"
imagestring = "\\166.2.126.227\International_Programs\Ethiopia\2017_01_20_mapupdate\imagery\eth_landsat_8_2016024.tif"
image = Raster(imagestring)
ExtObj = image.extent
clipExtent = "%d %d %d %d" % (ExtObj.XMin, ExtObj.YMin, ExtObj.XMax, ExtObj.YMax)
print clipExtent
arcpy.Clip_management(dem, clipExtent, demClip, "#", "NoData", "ClippingGeometry", "NO_MAINTAIN_EXTENT")
print "finished"
