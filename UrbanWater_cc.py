""""----------------------------------------------------------------------------
Name:         Urban Water Analysis
              Analysis with the core concepts
Purpose:      find buildings covered by distance and elevation
Project:      language for spatial computing
Author:       Kuhn et al. 2018, adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    coreconcepts based on arcpy -----------"""

from coreconcepts.utils import *

# load input data
area = makeObject('C:/area.shp')
dem = makeField('C:/dem.tif').restrictDomain(area, 'inside')
waterPoint = makeObject('C:/waterPoints.shp').restrictDomain(area, 'inside')
building = makeObject('C:/buildings.shp').restrictDomain(area, 'inside')

# set parameters
distance = 50
elevation = 3

# Question 1: What are the elevations of the water points?
waterPoint_elev = waterPoint.addProperty(dem)

# Question 2: What are the elevations of the buildings?
building_elev = building.addProperty(dem)

for wp in waterPoint_elev:

   # Question 3: Which buildings are within the distance of the water point?
   wp_buffer = wp.buffer(distance, 'Meters')
   buildings_in_d = building_elev.restrictDomain(wp_buffer, 'inside')

   # Question 4: Which buildings are within the elevation parameter of the  water point?
   wpElev = wp.get('RASTERVALU')
   sql = 'RASTERVALU >= ' + str(wpElev - elevation) + ' AND ' + 'RASTERVALU <= ' + str(wpElev + elevation)
   WDWE = buildings_in_d.withProperty(sql)

   # save output
   id = wp.get('FID')
   WDWE.save('C:/out', 'WDWE_' + str(id), '.shp')
