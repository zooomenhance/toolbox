# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:38:10 2018

@author: adamclark
"""
import arcpy
from arcpy import env

env.workspace = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null"

# Load segments for each run
shp_car = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/car_rev_p2null_majority/CAR_REV_2018_11_15.shp"

shp_car_b = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/car_rev_buffer_p2null_majority/CAR_REV_2018_11_15_buffer.shp"

shp_sfe = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null/sfe_rev_p2null_majority/SFE_REV_2018_11_15.shp"

shp_sfe_b = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/santafe/deliverables/height_reassignment/classification_based_p2null/sfe_rev_buffer_p2null_majority/SFE_REV_2018_11_15_buffer.shp"

zs_sfe = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/car_rev_clip_p2null_majority_band1.dbf"
zs_sfe_b = "//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/carson/deliverables/height_reassignment/classification_based_p2null/car_rev_buffer_p2null_majority_band1.dbf"

#set up order of fields with old field first and new field last
fieldsCar = ['Wdy_Sizemj', "Lifeform", "Data_Sourc"]
fieldsSFE= ['Wdy_Sizemj', "Lifeform", "MAJORITY"]


def updateField_carson(fc, fieldsCar):
# Create update cursor for feature class 
    with arcpy.da.UpdateCursor(fc, fieldsCar) as cursor:
        # For each row, evaluate the code value (index position 
        # of 0), and update newcode (index position of 1)
        for row in cursor:        
            if row[2] == "PI":
                row[1] = row[0]
            elif row[0] == "1" and row[2] == "Lidar2017":
                row[0] = "1) 0-.5 meters"
            elif row[0] == "2" and row[2] == "Lidar2017":
                row[0] = "2) .5-5 meters"
            elif row[0] == "3" and row[2] == "Lidar2017":
                row[0] = "3) 5-12 meters"
            elif row[0] == "4" and row[2] == "Lidar2017":
                row[0] = "4) 12+ meters"
    
            # Update the cursor with the updated list
            cursor.updateRow(row)
            print (row)
    print ("updated Veg Height")
    
    with arcpy.da.UpdateCursor(fc, fieldsCar) as cursor:
        # For each row, evaluate the code value (index position 
        # of 0), and update newcode (index position of 1)
        for row in cursor:
          
            if row[1] == "Herb" or row[1] == "Water" or row[1] == "Sparsely Vegetated":
                row[0] = "0) non Tree-Shrub"
            cursor.updateRow(row)
            print (row)
    print("updated non Tree-Shrub calls")
    
    print("All done!")
updateField_carson(shp_car, fieldsCar)   
updateField_carson(shp_car_b, fieldsCar)  
    
    
    
       
def updateField_sfe(fc, zs, fieldsSFE):
    #arcpy.JoinField_management(fc, "FID", zs, "FID_", ["FID_","MAJORITY"])    

    
# Create update cursor for feature class 
    with arcpy.da.UpdateCursor(fc, fieldsSFE) as cursor:
        # For each row, evaluate the code value (index position 
        # of 0), and update newcode (index position of 1)
        for row in cursor:        
            if row[2] == 1:
                row[0] = "1) 0-.5 meters"
            elif row[2] == 2:
                row[0] = "2) .5-5 meters"
            elif row[2] == 3:
                row[0] = "3) 5-12 meters"
            elif row[2] == 4:
                row[0] = "4) 12+ meters"
    
            # Update the cursor with the updated list
            cursor.updateRow(row)
            print (row)
    print ("updated Veg Height")
    
    with arcpy.da.UpdateCursor(fc, fieldsSFE) as cursor:
        # For each row, evaluate the code value (index position 
        # of 0), and update newcode (index position of 1)
        for row in cursor:
          
            if row[1] == "Herb" or row[1] == "Water" or row[1] == "Sparsely Vegetated":
                row[0] = "0) non Tree-Shrub"
            cursor.updateRow(row)
            print (row)
    print("updated non Tree-Shrub calls")
    
    print("All done!")
    
updateField_sfe(shp_sfe, zs_sfe, fieldsSFE)   
updateField_sfe(shp_sfe_b, zs_sfe_b, fieldsSFE)  
    