# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:03:24 2019

@author: adamclark
"""
import arcpy
         
import csv

import time
from arcpy import env
env.workspace = "Y:/Data/LiDAR/Phase2/POW_PHASE2_METRICS"
f = open("Y:/Data/LiDAR/Phase2/POW_PHASE2_METRICS/listimg.csv",'r')
csv = csv.reader(f)
csv_list = list(csv)
total_files = sum(1 for row in csv_list)
count = 0
count2 = 1
file = "Y:/Data/LiDAR/Phase2/POW_PHASE2_METRICS/"
output = "within_pow"
folder = ['Southwest/reprojected_resampled_ac/','Southeast/reprojected_resampled_ac/','Central/reprojected_resampled_ac/','Northern/reprojected_resampled_ac/']
clip_boundary = "Y:/Boundary/POW_Final_AOI/POW_Final_AOI.shp"
startTotal = time.clock()
for row in csv_list:
    start = time.clock()
    count = count + 1
    print (str(count) + "/" + str(total_files))
    #mosaic_in = "'" + file + folder[0]+ row[0] + "';"+"'" + file + folder[1]+ row[0] + "';"+"'" + file + folder[2]+ row[0] + "';"+"'" + file + folder[3]+ row[0] + "'"
    #print (mosaic_in)
    #arcpy.MosaicToNewRaster_management(mosaic_in, output, row[0][:-4] + "_mosaic.img", 26931, "32_BIT_FLOAT", "5", "1", "LAST","FIRST")
    if count >273:
        count2 = count2+1
        arcpy.Clip_management("Y:/Data/LiDAR/Phase2/POW_PHASE2_METRICS/within_pow/" + row[0][:-4] + "_mosaic.img", '#',  "Y:/Data/LiDAR/Phase2/POW_PHASE2_METRICS/within_pow/clip/" + row[0][:-4] + "_mosaic_clip.img", clip_boundary, "#", "ClippingGeometry", "MAINTAIN_EXTENT")
        print ('Finished working on' + row[0])
    if count2%2 == 0:
        print ("total time elapsed: %.3f min" %  ((time.clock() - startTotal)/60))
        print ("estimated time remaining: %.3f min" % ((((time.clock() - startTotal)/count2) * (total_files - count2))/60))
print ("Finished Operation")
