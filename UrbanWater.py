""""----------------------------------------------------------------------------
Name:         Urban Water Analysis
              Conventional analysis
Purpose:      find buildings covered by distance and elevation
Project:      language for spatial computing
Author:       ICRC (2017), adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    arcpy
-------------------------------------------------------------------------------"""

from arcpy import CheckOutExtension, env, SelectLayerByLocation_management, FeatureToPoint_management, CopyFeatures_management, JoinField_management, SelectLayerByAttribute_management
from arcpy.sa import ExtractValuesToPoints
from arcpy.da import SearchCursor

env.overwriteOutput = True
CheckOutExtension("Spatial")

# load input data
area = 'C:/area.shp'
dem = 'C:/dem.tif'
waterPoint = 'C:/waterPoints.shp'
building = 'C:/buildings.shp'

# set parameters
distance = 50
elevation = 3

# select water points within area
waterPoint_inArea = SelectLayerByLocation_management(waterPoint, 'INTERSECT', area)

# select buildings within area
building_inArea = SelectLayerByLocation_management(building, 'INTERSECT', area)

# elevation of waterPoints
waterPoint_elev = ExtractValuesToPoints(waterPoint_inArea, dem, 'in_memory/wp_elev')

# calculate elevation of buildings (using centroid)
building_point = FeatureToPoint_management(building_inArea, 'in_memory/building_point', 'CENTROID')
building_pt_elev = ExtractValuesToPoints(building_point, dem, 'in_memory/building_pt_elev')
building_elevation = CopyFeatures_management(building_inArea, 'in_memory/building_elevation')
JoinField_management(building_elevation, 'FID', building_pt_elev, 'FID', 'RASTERVALU')

cursor = SearchCursor(waterPoint_elev, ['OID@', 'SHAPE@', 'RASTERVALU'])
for wp in cursor:
   geom = wp[1]

   # select buildings within distance
   D = str(distance) + ' Meters'
   inDistance = SelectLayerByLocation_management(building_elevation, 'WITHIN_A_DISTANCE', geom, D)

   # select buildings within elevation
   sql = 'RASTERVALU >= ' + str(wp [2] - elevation) + ' AND ' + 'RASTERVALU <= ' + str(wp[2] + elevation)
   WDWE = SelectLayerByAttribute_management(inDistance, 'SUBSET_SELECTION', sql)
   #  save output
   CopyFeatures_management(WDWE, 'C:/WDWE_' + str(wp [0]) + '.shp')
