# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:15:43 2019

@author: adamclark
"""
#
#from PIL import Image
#import glob
#import numpy as np
#
#imgs = glob.glob(r"C:\Users\ncate\Desktop\ari\*.tif")
#tile_size = 1024
#tiles_per_image = 10
#
#def rand_512(image, size):
#    w,h = image.size
#    new_col = np.random.randint(0, w-size)
#    new_row = np.random.randint(0, h-size)
#    box = (new_col, new_row, new_col+size, new_row+size)
#    cropped = image.crop(box)
#    return cropped
#
#for i in range(len(imgs)):
#    curr = Image.open(imgs[i])
#    for c in range(tiles_per_image):
#        new = rand_512(curr, tile_size)
#        new.save("C:/Users/ncate/Desktop/ari/cropped2/"+ str(i)+str(c)+".jpg")



import json

from PIL import Image

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.patches as patches

im = np.array(Image.open(r"C:\Users\adamclark\Downloads\00.jpg"))

json_loc = r"C:\Users\adamclark\Downloads\cate_clark_v7.json"

with open(json_loc) as json_file:

    x = json.load(json_file)


#print(json.dumps(x, indent = 4, sort_keys=True))

imgs = list(x['_via_img_metadata'].keys())
#
a = x['_via_img_metadata']
#print(a)
#r = a['regions']
#print(r)
rect_list = []
#
#for p in a['regions']:
#    print(p)
#    label = p['region_attributes']
#
#    #x = p['shape_attributes']['x']
#    print(x)
#
#    y = p['shape_attributes']['y']
#    print(y)
#
#    width = p['shape_attributes']['width']
#
#    height = p['shape_attributes']['height']

#    rect_list.append(patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none'))

#fig, ax = plt.subplots(1)
#
#for rect in rect_list:
#
#    ax.add_patch(rect)
#
#ax.imshow(im)
#
#plt.show()