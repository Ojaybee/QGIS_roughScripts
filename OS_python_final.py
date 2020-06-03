import os

#Get prefix
prefix = iface.activeLayer().name()[:3]
if "_" in prefix:
    layer = QgsProject.instance().mapLayersByName(prefix + "Building")
    path = layer[0].dataProvider().dataSourceUri()
    cleanPath = path[:path.rfind('|')]
    (myDirectory, fileName) = os.path.split(cleanPath) 

    roadFile = myDirectory + r'\\' + prefix + "Road.shp"
    for i in range(5):
        road = iface.addVectorLayer(roadFile, "", "ogr")
    
    roundaboutFile = myDirectory + r'\\' + prefix + "Roundabout.shp"
    roundabout = iface.addVectorLayer(roundaboutFile, "", "ogr")

root = QgsProject.instance().layerTreeRoot()
for child in root.children():
    basename = child.name()
    if "_" in basename[:3]:
        child.setName(basename[3:])
        
        


#Create clones of every layer
roundAbtClone1 = root.children()[0].clone()
roadClone1 = root.children()[1].clone()
roadClone2 = root.children()[2].clone()
roadClone3 = root.children()[3].clone()
roadClone4 = root.children()[4].clone()
roadClone5 = root.children()[5].clone()

adminClone = root.children()[6].clone()
buildClone = root.children()[7].clone()
ETClone = root.children()[8].clone()
foreShoreClone = root.children()[9].clone()
funcSiteClone = root.children()[10].clone()
glassHouseClone = root.children()[11].clone()
mJuncClone = root.children()[12].clone()
nPlaceClone = root.children()[13].clone()
ornamentClone = root.children()[14].clone()
railStationClone = root.children()[15].clone()
railTrack = root.children()[16].clone()
railTunnel =root.children()[17].clone()
roadClone6 = root.children()[18].clone()  
roadTunClone = root.children()[19].clone()
roundAbtClone2 = root.children()[20].clone()
spotHeightClone = root.children()[21].clone()
surfWaterAreaClone = root.children()[22].clone()
surfWaterLineClone = root.children()[23].clone()
tidalBoundaryClone = root.children()[24].clone()
tidalWaterClone = root.children()[25].clone()
woodClone = root.children()[26].clone()

#reorder layers and rename roads and roundabouts
root.insertChildNode(27, funcSiteClone)
root.insertChildNode(28, mJuncClone)
root.insertChildNode(29, railStationClone)
root.insertChildNode(30, nPlaceClone)
root.insertChildNode(31, spotHeightClone)
root.insertChildNode(32, adminClone)
root.insertChildNode(33, ETClone)
root.insertChildNode(34, railTunnel)
root.insertChildNode(35, roadTunClone)
root.insertChildNode(36, railTrack)
root.insertChildNode(37, roadClone1)
root.insertChildNode(38, roadClone2)
root.insertChildNode(39, roadClone3)
root.insertChildNode(40, roadClone4)
root.insertChildNode(41, roundAbtClone1)
root.insertChildNode(42, roadClone5)
root.insertChildNode(43, roadClone6)
root.insertChildNode(44, roundAbtClone2)
root.insertChildNode(45, glassHouseClone)
root.insertChildNode(46, buildClone)
root.insertChildNode(47, tidalBoundaryClone)
root.insertChildNode(48, surfWaterLineClone)
root.insertChildNode(49, ornamentClone)
root.insertChildNode(50, surfWaterAreaClone)
root.insertChildNode(51, woodClone)
root.insertChildNode(52, foreShoreClone)
root.insertChildNode(53, tidalWaterClone)

root.children()[37].setName("Road (Level 2 - Fill)")
root.children()[38].setName("Road (Level 2 - Casing)")
root.children()[39].setName("Road (Level 1 - Fill)")
root.children()[40].setName("Road (Level 1 - Casing)")
root.children()[41].setName("Roundabout (Fill)")
root.children()[42].setName("Road (Level 0 - Fill)")
root.children()[43].setName("Road (Level 0 - Casing)")
root.children()[44].setName("Roundabout (Casing)")

for i in range(27):
    i = 26 - i
    layer = root.children()[i]
    root.removeChildNode(layer)
    
for layer in QgsProject.instance().mapLayers().values():
    path = layer.dataProvider().dataSourceUri()
    cleanPath = path[:path.rfind('|')]
    (myDirectory, fileName) = os.path.split(cleanPath)
    uri = myDirectory + r'\\' + layer.name() + '.qml'
    layer.loadNamedStyle(uri) 


