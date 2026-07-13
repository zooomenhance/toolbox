import arcpy

infc = r'C:\Users\adamclark\Desktop\deleteme\1008_1_domain.shp'
inraster = r'C:\Users\adamclark\Desktop\deleteme\1008_1_domain.shp'
outfc = r'C:\Users\adamclark\Desktop\deleteme\1008_1_domain_300bufpy.shp'
bufferDistance = -300

arcpy.Buffer_analysis(infc, outfc, bufferDistance, "", "", "ALL")
print "buffer complete"
arcpy.RasterDomain_3d("dtm_grd", "raster_domain.shp", "POLYGON")
print "domain complete"
