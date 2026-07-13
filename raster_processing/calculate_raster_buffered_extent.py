import arcpy

elevRaster = arcpy.sa.Raster('C:/Users/adamclark/Desktop/deleteme/1008_1.tif')
myExtent = elevRaster.extent
myExtentXMin = myExtent.XMin
newXMin = myExtent.XMin + 300
newYMin = myExtent.YMin + 300
newXMax = myExtent.XMax - 300
newYMax = myExtent.YMax - 300
print myExtent
print myExtentXMin
print newXMin, newYMin, newXMax, newYMax
