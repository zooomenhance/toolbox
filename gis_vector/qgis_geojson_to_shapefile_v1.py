##input into qgis py console. Will convert everything in your TOC THATS TURNED ON to shp
myDir = 'E:/downloads/microsoft_building_footprints/shp/'

for vLayer in iface.mapCanvas().layers():
    QgsVectorFileWriter.writeAsVectorFormat( vLayer, myDir + vLayer.name() + ".shp", "utf-8", vLayer.crs(), "ESRI Shapefile" )