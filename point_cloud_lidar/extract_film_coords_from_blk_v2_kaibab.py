################################################################################
#
#                    USER INPUTS
#
################################################################################

BlockFile = 'C:/Users/adamclark/Downloads/Block Files/kaibab1.blk'
OutputFile = 'I:/photoscan_kaibab/kai_n/block_file/kaibab1_principalpoints.txt'
hfatest = '//166.2.126.25/R4_VegMaps/VegMapping_Tools/HFA_Extractor/hfatest.exe'

################################################################################

import subprocess

# Run hfatest.exe and save the output to the HFA_Info variable.
process = subprocess.Popen(hfatest + ' -dt ' + BlockFile, stdout = subprocess.PIPE, shell = True)
HFA_Info = process.communicate()[0]

# The keys to the ImageDict variable are the names of the images.  The values
# are the list of coordinates for each image.
ImageDict = {}

# FilmToImage is changed to True when the FileToImage section is found.
# FilmToImage is changed to False when a new image is encountered.
FilmToImage = False

# Go through the HFA info and find the image name and the image coordinates.
# Save this information to the ImageDict dictionary.
for line in HFA_Info.split('\n'):

    # Remove the \r at the end of the line.
    line = line.split('\r')[0]

    # If an image is encountered, change the FilmToImage to False, get the name
    # of the image, and initialize ImageDict.
    if (line.find('ImageName') >= 0):
        FilmToImage = False
        ImageName = line[line.find('=')+3:len(line)-1]
        if (ImageDict.get(ImageName) == None):
            ImageDict[ImageName] = []
        else:
            print 'this is a duplicate image:',ImageName

    # The FilmToImage section has been found if the conditional is True.
    if (line.find('FilmToImage') >= 0):
        FilmToImage = True

    # Get the coordinates.
    if (FilmToImage) & (line.find('polycoefvector[0]') >= 0):
        number = line.split(' ')[-1]
        ImageDict[ImageName].append(number)
    if (FilmToImage) & (line.find('polycoefvector[1]') >= 0):
        number = line.split(' ')[-1]
        ImageDict[ImageName].append(number)

# Extract the image names from the ImageDict and sort them.
Images = ImageDict.keys()
Images.sort()

# Create the output text file.
Output = open(OutputFile,'w')

# Go through the images and write the information to the OutputFile.
for image in Images:
    Output.write(image + '\t' + ImageDict[image][0] + '\t' + ImageDict[image][1] + '\n')
    print image,ImageDict[image]

# Close the file.
Output.close()
        
print 'Done!'        
