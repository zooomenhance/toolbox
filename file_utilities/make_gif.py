#----------------------------------------------------------
#                       make_gif.py
#----------------------------------------------------------
import os
import imageio

# User Parameters
image_dir = r'Z:\Projects\06_LCMS_4_NFS\R10\12_ChugachNF_Kenai\04_TechTransfer\04_Graphics_Animations\gif-outputs\mosaics\kenai1_lcms_mosaics' # where to find the input gifs
file_extension = '.png' # file extension for the input images
output_dir = r'C:\Users\leahcampbell\home\lcms\gif_test_dir' # where to save the final gif
gif_name = 'test_gif' # what you want the name of the final gif to be
frame_duration = 1.3 # duration of each frame, I think in seconds?

#Returns all files containing an extension or any of a list of extensions
#Can give a single extension or a list of extensions
def glob(Dir, extension):
    out_list = []
    if type(extension) != list:
    	extension = [extension]
    for ext in extension:
    	for file in os.listdir(Dir):
    		if os.path.splitext(file)[1] == ext:
    			out_list.append(os.path.join(Dir, file))
    return out_list

images = glob(image_dir, file_extension)
out_stack = os.path.join(output_dir, gif_name+'.gif')
if os.path.exists(output_dir) == False:
    os.mkdir(output_dir)

if len(images) > 0:
    print('Creating:', gif_name)
    frames = [imageio.imread(fn) for fn in images]   
    imageio.mimsave(out_stack, frames, duration = frame_duration)
    print(out_stack)
    frames = None