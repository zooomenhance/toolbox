# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:49:57 2018

@author: adamclark
"""

##Join a table and copy the records over to a new field then clean up table


import arcpy
from arcpy import env

# Set environment settings and define data
env.workspace = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null"
##feature class to join table to
fc = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null/sfe_rev_p2null_majority/SFE_REV_2018_11_15.shp"
##table to use as join to feature class
table = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null/sfe_rev_2018_11_15_buffer_lidarp2null_zs.csv"
## name of field in table to copy data
old_field = "text"
## name of new field to create and add data
new_field = "text"
fields= ['id_old', "id_new", "field_old", "field_new"]

## reclassify raster
#arcpy.Reclassify (in_raster, reclass_field, remap, {missing_values})







def add_join(fc, table, new_field, old_field):
    ##new field to copy data over to 
    arcpy.AddField_management(fc, "wdy_ht_sd", "DOUBLE")
    arcpy.AddField_management(fc, "Wdy_Size", "TEXT", "", "", "32", "", "NULLABLE", "NON_REQUIRED", "")
    ##join based FID values
    arcpy.JoinField_management(fc, "FID", table, "FID")
    
    
    
def copy_data(fc, fields):
# Create update cursor for feature class 
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        # For each row, evaluate the code value (index position 
        # of 0), and update newcode (index position of 1)
        for row in cursor:    
            print (row)
            if row[0] == row[1]:
                row[2] = row[3]
            # Update the cursor with the updated list
            cursor.updateRow(row)
            print (row)
    print ("updated Veg Height")