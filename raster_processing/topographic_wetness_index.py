import arcpy, math
arcpy.CheckOutExtension("Spatial")
	
# Define workspace and set input and output files
arcpy.env.workspace = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\TopographicWetnessIndex")
inDEM = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\pow_lidar_dtm_5m_reproj.img")
outTWI = (r"\\166.2.125.166\R10_VegMaps\TongassNF\PrinceOfWales\Data\LiDAR\pow_phases_combined\pow_lidar_5m\TopographicWetnessIndex\pow_lidar_twi.img")

# Intermediates
arcpy.AddMessage("Filling DEM.\n")
DEM_filled = arcpy.sa.Fill(inDEM)
	
arcpy.AddMessage("Creating flow direction.\n")
outFlowDirection = arcpy.sa.FlowDirection(DEM_filled, "FORCE")
	
	
arcpy.AddMessage("Creating flow accumulation.\n")
#outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "FLOAT") + 1 
outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "INTEGER") + 1 
	
arcpy.AddMessage("Creating slope.\n")
slope = arcpy.sa.Slope(DEM_filled)
	

arcpy.AddMessage("Converting slope in degrees to slope in radians")
# 2Pi radians = 360 degrees
# Pi radians = 180 degrees
# conversion: Pi radians/180 degress
slope_radians = slope * math.pi/180.0
	
# Output
arcpy.AddMessage("Creating TWI\n")
TWI = arcpy.sa.Ln(outFlowAccumulation / (arcpy.sa.Tan(slope_radians)+.01))
TWI.save(outTWI)
arcpy.AddMessage("Saved TWI. Done.")
