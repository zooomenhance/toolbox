import os
##script will replace certain characters in a folder of files. save script in the same directory
##you want to change and change the parameters. In this script it will take the string '_clip'
##and replace it with nothing. Script should run over a few thousand files in less than a second. 
[os.rename(f, f.replace('_clip', '')) for f in os.listdir('.') if not f.startswith('.')]
