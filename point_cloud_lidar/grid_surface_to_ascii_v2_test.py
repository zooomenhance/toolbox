import os

# Directory containing .las files
folder = "G:\\RMAP_2017\\Coronado_NF\\2017_01_23_cleanup\\combined\\las"

# Name of .bat file you are creating (full location)
batfile = "G:\\RMAP_2017\\Coronado_NF\\scripts\\2017_01_23_cleanup_GridSurface_cor_NF.bat"

# FilterData parameters (standard deviation, window size)
# stdDev = 2.0
# windowSize = 50

# Initialize list of .las files and count of files
las_files = []
count = 0

# Go through folder, find all .las files and add to list
for filename in os.listdir(folder):
    if filename.endswith(".las"):
        las_files.append(filename)
        count = count + 1

#print(las_files)
        
print('Number of .las files: {}'.format(count))
# print('Using standard deviation = {}\n      window size = {}'.format(stdDev,windowSize))

# Open .bat file to write FilterData command for each .las file
# Filtered .las files are named 'filtered_[original].las' where
# [original] is the original filename
with open(batfile, 'w') as f:
    for filename in las_files:
        outputfile = filename[:-4] +'.dtm'
        line = 'GridSurfaceCreate ' + folder + '\\' + outputfile + ' 2 m m 1 12 2 2 ' + folder + '\\' + filename + '\n'
        line2 = 'DTM2ASCII /raster ' + folder + '\\' + outputfile + '\n'
        f.write(line)
        f.write(line2)

print('File written to\n {}'.format(batfile))
print('Closed: {}'.format(f.closed))
