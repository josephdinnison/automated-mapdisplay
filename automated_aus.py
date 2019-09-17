
#### The first section sets up the workspace, selects a default geodatabase, and enters Map Document properties ####


import arcpy

mD = arcpy.mapping.MapDocument('CURRENT')
dF = mD.activeDataFrame
fcs = arcpy.ListFeatureClasses()
arcpy.env.workspace = r'C:\Users\Joey\Desktop\Work\ArcMap projects\test 8-20\test820.gdb'
mD.author = 'Joseph Dinnison'
mD.title = 'A Quick Map of Australia'
mD.summary = "This is a basic map showing Australia's major cities and rivers, created using Arcpy"
mD.description = "Australia, officially the Commonwealth of Australia, is a sovereign country comprising the mainland of the Australian continent, the island of Tasmania, and numerous smaller islands. It is the largest country in Oceania and the world's sixth-largest country by total area."
mD.credits = 'naturalearthdata.com, udemy.com'
mD.tags = 'Australia, Rivers, Cities'
mD.hyperlinkBase = 'josephdinnison.com'


#### This second section adds layers (from the geodatabase) to the dataframe and defines a coordinate system ####


ausLayer = arcpy.mapping.Layer('C:/Users/Joey/Desktop/Work/ArcMap projects/test 8-20/test820.gdb/Australia')
riverLayer = arcpy.mapping.Layer('C:/Users/Joey/Desktop/Work/ArcMap projects/test 8-20/test820.gdb/WorldRivers')
cityLayer = arcpy.mapping.Layer('C:/Users/Joey/Desktop/Work/ArcMap projects/test 8-20/test820.gdb/WorldCities')

arcpy.mapping.AddLayer(dF, ausLayer, "BOTTOM")
arcpy.mapping.AddLayer(dF, riverLayer, "TOP")
arcpy.mapping.AddLayer(dF, cityLayer, "TOP")


sr = arcpy.SpatialReference("GDA 1994 Australia Albers")
arcpy.DefineProjection_management(riverLayer, sr)
arcpy.DefineProjection_management(ausLayer, sr)
arcpy.DefineProjection_management(cityLayer, sr)


#### This third section clips the two "world" layers to the Australia layer ####


arcpy.Clip_analysis("WorldCities", "Australia", "cityclip1")
arcpy.Clip_analysis("WorldRivers", "Australia", "riverclip1")


#### This fourth section removes the original layers used for the clip ####


for dF in arcpy.mapping.ListDataFrames(mD):
    for lyr in arcpy.mapping.ListLayers(mD, "", dF):
        if lyr.name == "WorldCities":
            arcpy.mapping.RemoveLayer(dF, lyr)
        if lyr.name == "WorldRivers":
            arcpy.mapping.RemoveLayer(dF, lyr)

        
arcpy.RefreshTOC()
arcpy.RefreshActiveView()


#### This fifth section labels the cities feature ####


cityLayer = arcpy.mapping.ListLayers(mD, "cityclip1")[0]
if cityLayer.supports("NAME"):
    for lblclass in cityLayer.labelClasses:
        lblclass.showClassLabels = True
cityLayer.showLabels = True

#riverLayer = arcpy.mapping.ListLayers(mD, "riverclip1")[0]
#if riverLayer.supports("name"):
#    for lblclass in riverLayer.labelClasses:
#        lblclass.showClassLabels = True
#riverLayer.showLabels = True


arcpy.RefreshActiveView()


#### Finally, when all these tasks are finished running, a prompt to save the .mxd will appear ####


mD.save()
del mD



