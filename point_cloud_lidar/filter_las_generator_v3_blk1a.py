import os

# Directory containing .las files
folder = "D:\\Coconino_phodar\\blk1a"

# Name of .bat file you are creating (full location)
batfile = "D:\\Coconino_phodar\\scripts\\FilterData_1a.bat"

# FilterData parameters (standard deviation, window size)
stdDev = 2.0
windowSize = 50

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
print('Using standard deviation = {}\n      window size = {}'.format(stdDev,windowSize))

# Open .bat file to write FilterData command for each .las file
# Filtered .las files are named 'filtered_[original].las' where
# [original] is the original filename
with open(batfile, 'w') as f:
    for filename in las_files:
        outputfile = 'filtered_' + filename
        line = 'FilterData outlier ' + str(stdDev) + ' ' + str(windowSize) + ' ' + \
               folder + '\\' + outputfile + ' ' + folder + '\\' + filename + '\n'
        f.write(line)

print('File written to\n {}'.format(batfile))
print('Closed: {}'.format(f.closed))
