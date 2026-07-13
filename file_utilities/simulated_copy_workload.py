import csv
import time
import random

f = open("H:/donotdeleteme/scripts/Full_List.csv")
csv = csv.reader(f)
count = 0
for row in csv:
    count = count + 1
    print(count)
    time.sleep(random.randint(0,3))
    print(row[0])
    time.sleep(random.randint(0,3))
    fileName = str(row[0])
    inCopy = "H:/11-144_USFS_Wallow/Raw Image Scans/" + fileName
    outCopy = "H:/11-144_USFS_Wallow/RMAP/"+ fileName
    print(fileName)
    time.sleep(random.randint(0,3))
    print(inCopy)
    time.sleep(random.randint(0,3))
    print(outCopy)
    ##print(f)
    print('Finished working on ' + fileName)
print("Finished copying all .tif files")
