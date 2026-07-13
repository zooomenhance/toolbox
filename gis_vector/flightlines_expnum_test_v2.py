import arcpy

workspace = r"E:\RMAP_2017\getflightlines\COR_NF"
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True

flightlines = "613050_index_4-11-2.shp"
#flightlines_copy = "flightlines3 - Copy.shp"
RMAP = "RMAP_AZS_ COR_WORKING.shp"

existingValues = []

with arcpy.da.SearchCursor(flightlines,["EXPNUM"]) as cursor:
	for row in cursor:
		if row[0] not in existingValues:
			existingValues.append(row[0])
del cursor
existingValues = sorted(existingValues)
existingValues = list(reversed(existingValues))
print existingValues
for fl in existingValues:
	print fl
	if fl == existingValues[-1]:
		break
	#############################################################
	#Current row
	temp_fl1 = "temp_fl1"
	arcpy.MakeFeatureLayer_management(flightlines,temp_fl1)
	#Select in memory flightlines by attribute
	arcpy.SelectLayerByAttribute_management(temp_fl1,"NEW_SELECTION",'"EXPNUM"= \'' + fl + '\'')
	
	
	#next row
	flplus1 = existingValues[existingValues.index(fl) + 1]
	print(flplus1)
	temp_fl2 = "temp_fl2"
	arcpy.MakeFeatureLayer_management(flightlines,temp_fl2)
	#Select in memory flightlines by attribute
	arcpy.SelectLayerByAttribute_management(temp_fl2,"NEW_SELECTION",'"EXPNUM"= \'' + flplus1 + '\'')
	
	
	#Get intersect of the two rows.
	intersect1 = "intersect1.shp"
	arcpy.Intersect_analysis([temp_fl1,temp_fl2],intersect1)
	del temp_fl1
	del temp_fl2
	
	#Get intersect of the two rows and RMAP
	#Bring RMAP into memory
	temp_fl4 = "temp_fl4"
	arcpy.MakeFeatureLayer_management(RMAP,temp_fl4)
	intersect2 = "intersect2.shp"
	arcpy.Intersect_analysis([intersect1,RMAP],intersect2)
		
	#Select all rows that intersect the intersect2
	temp_fl3 = "temp_fl3"
	arcpy.MakeFeatureLayer_management(flightlines,temp_fl3)
	arcpy.SelectLayerByAttribute_management(temp_fl3,"NEW_SELECTION",'"EXPNUM"in (\'' + fl + '\',\'' + flplus1 + '\')')
	arcpy.SelectLayerByLocation_management(temp_fl3,"INTERSECT", intersect2,'','SUBSET_SELECTION')
	
	#Calculate 1 for all those selected
	arcpy.CalculateField_management(temp_fl3,"use_phodar",2)
	
	
	
	
	#Erase selection from RMAP
	erase_output = "temp_erase.shp"
	arcpy.Erase_analysis(RMAP,intersect2,erase_output)
	arcpy.Delete_management(RMAP)
	arcpy.CopyFeatures_management(erase_output,RMAP)
	arcpy.Delete_management(erase_output)
	
	del temp_fl3
	del temp_fl4
	del intersect1
	del intersect2

	
	
	
	
