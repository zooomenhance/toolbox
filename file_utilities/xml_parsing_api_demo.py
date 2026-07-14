# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 08:00:24 2019

@author: adamclark
"""
##example found here - https://www.geeksforgeeks.org/xml-parsing-python/

#Python code to illustrate parsing of XML files 
# importing the required modules 
import requests 
import xml.etree.ElementTree as ET 
import webbrowser


# url of rss feed - enter route number after "route=" in url below. Replace YOUR_UTA_API_TOKEN with your actual API token.
url = 'http://api.rideuta.com/SIRI/SIRI.svc/VehicleMonitor/ByRoute?route=472&onwardcalls=true&usertoken=YOUR_UTA_API_TOKEN'

# creating HTTP response object from given url 
resp = requests.get(url) 

# saving the xml file to folder and reading it
with open('uta_data.xml', 'wb') as f: 
	f.write(resp.content) 

xml = 'uta_data.xml'
# parsing the xml file for all bus location on route
api_results = ET.parse(xml)
root = api_results.getroot()
#iterates over root and produces all elements within xml
#for elem in root.iter():
#  print(elem.tag, elem.attrib)

#creates empty lists for adding lat long data from xml
long = []
lat = []
count=0
#find each bus location and adds it to empty list
for elem in root.iter(tag='{http://www.siri.org.uk/siri}Longitude'):
    count = count+1    
    #print(elem.tag, elem.attrib, elem.text)
    long.append(elem.text)
for elem in root.iter(tag='{http://www.siri.org.uk/siri}Latitude'):
    #print(elem.tag, elem.attrib, elem.text)
    lat.append(elem.text)

if count == 0:
    print("no active bus on route")

#creating dynamic google maps urls for each bus location
#for i in range(0,count):
#    #create URL 
#    url1 = "https://www.google.com/maps/place/40°45'55.7%22N+111°53'17.7%22W/@40.7712281,-111.8947902,15.46z/data=!4m6!3m5!1s0x0:0x0!7e2!8m2!3d"
#    laturl = lat[i]
#    url2 ="!4d"
#    longurl = long[i]
#    fullurl = url1 + str(laturl) + url2 + str(longurl)
#    webbrowser.open(fullurl, new=1, autoraise=True)

#creating a static image showing all current bus locations
        #create URL 

urlbase = "https://maps.googleapis.com/maps/api/staticmap?center=40.766862, -111.887444&zoom=15&size=1500x1500"
urlpoints = ""
urlkey = '&key=YOUR_GOOGLE_MAPS_API_KEY'
for i in range(0,count):
    urlpoints = urlpoints + "&markers=" + str(lat[i]) + "," + str(long[i])
print(urlpoints)
fullstaticurl = urlbase + urlpoints + urlkey
print(fullstaticurl)
webbrowser.open(fullstaticurl, new=1, autoraise=True)
