# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:49:07 2018

@author: adamclark
"""


# Use UpdateCursor to update a field value by evaluating the values of other fields.

import arcpy
from arcpy import env
# Set environment settings
env.workspace = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null"
fc = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/CAR_REV_2018_11_15.shp"
zs = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/car_rev_2018_11_15_lidarp2null_zs.txt"
# add new fields - THIS WILL WRITE OVER EXISTING FIELDS WITH SAME NAMES
arcpy.AddField_management(fc, "wdy_ht_m", "DOUBLE")
arcpy.AddField_management(fc, "wdy_ht_sd", "DOUBLE")
arcpy.AddField_management(fc, "Wdy_Size", "TEXT", "", "", "32", "", "NULLABLE", "NON_REQUIRED", "")
#arcpy.AddField_management(fc, "Size_Class", "TEXT", "", "", "32", "", "NULLABLE", "NON_REQUIRED", "")

print ("created fields")

#set up order of fields with old field first and new field last
fieldsVH = ['wdy_ht_m', 'Wdy_Size']
##fieldsCC = ['cover_mean', 'Canopy_Cover', 'Data_Source', 'new_cc']
##fieldsLF = ['LF', 'Canopy_Cover', 'Size_Class']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fieldsVH) as cursor:
    # For each row, evaluate the code value (index position 
    # of 0), and update newcode (index position of 1)
    for row in cursor:
        if row[0] <= .5:
            row[1] = "1) 0-.5 meters"
        elif row[0] <= 5 and row[0] > .5:
            row[1] = "2) .5-5 meters"
        elif row[0] <= 12 and row[0] > 5:
            row[1] = "3) 5-12 meters"
        elif row[0] > 12:
            row[1] = "4) 12+ meters"
#        elif row[3] == "0-.5 meters" and row[2] == "PI":
#            row[1] = "1) 0-.5 meters"
#        elif row[3] == ".5-5 meters" and row[2] == "PI":
#            row[1] = "2) .5-5 meters"
#        elif row[3] == "5-12 meters" and row[2] == "PI":
#            row[1] = "3) 5-12 meters"
#        elif row[3] == "12+ meters" and row[2] == "PI":
#            row[1] = "4) 12+ meters"

        # Update the cursor with the updated list
        cursor.updateRow(row)
        print (row)
print ("updated Veg Height")
#
## Create update cursor for feature class 
#with arcpy.da.UpdateCursor(fc, fieldsCC) as cursor:
#    # For each row, evaluate the code value (index position 
#    # of 0), and update newcode (index position of 1)
#    for row in cursor:
#        if row[0] <= .25 and row[2] == "Lidar2017":
#            row[1] = "1) 10-25%"
#        elif row[0] <= .5 and row[0] > .25 and row[2] == "Lidar2017":
#            row[1] = "2) 25-50%"
#        elif row[0] <= .75 and row[0] > .5 and row[2] == "Lidar2017":
#            row[1] = "3) 50-75%"
#        elif row[0] > .75 and row[2] == "Lidar2017":
#            row[1] = "4) 75-100%"
#        elif row[3] == "10-25%" and row[2] == "PI":
#            row[1] = "1) 10-25%"
#        elif row[3] == "25-50%" and row[2] == "PI":
#            row[1] = "2) 25-50%"
#        elif row[3] == "50-75%" and row[2] == "PI":
#            row[1] = "3) 50-75%"
#        elif row[3] == "75-100%" and row[2] == "PI":
#            row[1] = "4) 75-100%"
#
#        # Update the cursor with the updated list
#        cursor.updateRow(row)
#        print row
#print "updated Canopy Cover"
#
## Create update cursor for feature class 
#with arcpy.da.UpdateCursor(fc, fieldsLF) as cursor:
#    # For each row, evaluate the code value (index position 
#    # of 0), and update newcode (index position of 1)
#    for row in cursor:
#      
#        if row[0] == "Herb" or row[0] == "Water" or row[0] == "Barren":
#            row[1] = "0) non Tree-Shrub"
#        if row[0] == "Herb" or row[0] == "Water" or row[0] == "Barren":
#            row[2] = "0) non Tree-Shrub"
#        # Update the cursor with the updated list
#        cursor.updateRow(row)
#        print row
#print "updated non Tree-Shrub calls"

print "All done!"
