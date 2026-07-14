import gdal

filepath = r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\pow_lidar_chm_5m.img"

# Open the file:
raster = gdal.Open(filepath)

# Check type of the variable 'raster'
type(raster)

# Projection
lidarprj = raster.GetProjection()
#print (lidarprj)

# Dimensions
raster.RasterXSize
raster.RasterYSize

# Number of bands
raster.RasterCount

# Metadata for the raster dataset
raster.GetMetadata()

# Read the raster band as separate variable
band = raster.GetRasterBand(1)

# Check type of the variable 'band'
type(band)

# Data type of the values
gdal.GetDataTypeName(band.DataType)

ifsarfile = r'\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\IfSAR\derivatives\ifsar_slope_degree_pow_5m.img'

openifsar = gdal.Open(ifsarfile)

ifsarprj = openifsar.GetProjection()
#print(ifsarprj)

dataset = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\IfSAR\derivatives\ifsar_slope_degree_pow_5m.img")
spatial_ref = arcpy.Describe(dataset).spatialReference
print (spatial_ref)
