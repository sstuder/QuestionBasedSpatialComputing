""""----------------------------------------------------------------------------
Name:         objects.py
Purpose:      coreconcepts library
Project:      language for spatial computing
Author:       Kuhn et al. 2018, adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    os, coreconcepts, arcpy -----------"""

import os
from coreconcepts.coreconcepts import CcObject
from coreconcepts import utils
from arcpy import Buffer_analysis, Describe, Delete_management, CopyFeatures_management, ListFields, FeatureToPoint_management, JoinField_management, SelectLayerByLocation_management, SelectLayerByAttribute_management, MakeFeatureLayer_management
from arcpy.sa import ExtractValuesToPoints
from arcpy.da import SearchCursor

class ArcShpObject(CcObject):
    """
    Concrete class for core concept 'object'
    For handling .shp files and feature classes of a geodatabase
    """

    def __init__(self, filepath, objIndex, domain):
        super().__init__(filepath, objIndex, domain)
        self.filepath = filepath
        self.sObj = objIndex
        self.domain = domain
        self.filename = os.path.basename(filepath)
        self.OIDs = SearchCursor(self.filepath, "OID@")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_FID = next(self.OIDs)[0]
        except StopIteration:
            self.OIDs = SearchCursor(self.filepath, "OID@")
            raise StopIteration
        next_filepath = f"{self.filepath}_FID={next_FID}"
        MakeFeatureLayer_management(self.filepath, next_filepath)
        SelectLayerByAttribute_management(next_filepath, "NEW_SELECTION", f"FID={next_FID}")
        return ArcShpObject(next_filepath, id(next_filepath), self.domain)

    def buffer (self, distance, unitType ):
        """
        Buffer input object
        @param distance: buffer distance
        @param unitType: unit type
        """

        # determine temporary unique file
        distName = str(distance)
        distName2 = distName.replace(".", "_")
        print("distName2", distName2)
        name = "buf_" + str(self.sObj) + distName2
        outputLocation = "in_memory\\" + name

        # calculate buffer
        concatDistance = str(distance) + " " + unitType
        Buffer_analysis(self.filepath, outputLocation, concatDistance)
        bufObj = utils.makeObject(outputLocation)

        # update cc instance's attributes
        desc = Describe(outputLocation)
        bufObj.domain = desc.extent
        bufObj.filepath = outputLocation
        bufObj.filename = os.path.basename(outputLocation)

        return bufObj

    def restrictDomain(self, object, operation):
        """
        Restricts current instance's domain based on object's domain
        @param object: extent to which the object is restricted
        @param operation: valid options: "inside", "outside"
        """

        name = "restDom_" + str(self.sObj)
        outputLocation = "in_memory\\" + name

        if operation == 'inside':
            # select by location
            select = SelectLayerByLocation_management(self.filepath, "INTERSECT", object.filepath)
            CopyFeatures_management(select, outputLocation)
            restDom = utils.makeObject(outputLocation)

        elif operation == 'outside':
            # select by location
            sel = SelectLayerByLocation_management(self.filepath, "INTERSECT", object.filepath)
            select = SelectLayerByLocation_management(sel, "INTERSECT", object.filepath, "", "SWITCH_SELECTION")
            CopyFeatures_management(select, outputLocation)
            restDom = utils.makeObject(outputLocation)

        else:
            raise NotImplementedError(operation)

        # update cc instance's attributes
        desc = Describe(outputLocation)
        restDom.domain = desc.extent
        restDom.filepath = outputLocation
        restDom.filename = os.path.basename(outputLocation)

        return restDom

    def get(self, prop):
        """
        :param: name of the property
        :returns: value of property in the object
        """

        with SearchCursor(self.filepath, prop) as cursor:
            for row in cursor:
                return row[0]

    def addProperty(self, in_raster):
        """
        get value of a field and write it to a column named RASTERVALU in the object
        @param in_raster: raster where the value is taken from
        """

        desc = Describe(self.filepath)
        name = "addProperty" + str(self.sObj)
        outputLocation = "in_memory\\" + name

        if desc.shapeType == "Point":
            ExtractValuesToPoints(self.filepath, in_raster.filepath, outputLocation)
            addProperty = utils.makeObject(outputLocation)

        elif desc.shapeType == "Line":
            raise NotImplementedError(desc.shapeType)

        elif desc.shapeType == "Polygon":
            polyToPoint = "in_memory\\polyToPoint_" + str(self.sObj)
            FeatureToPoint_management(self.filepath, polyToPoint, "CENTROID")
            valueToPoint = "in_memory\\valueToPoint_" + str(self.sObj)
            ExtractValuesToPoints(polyToPoint, in_raster.filepath, valueToPoint)
            CopyFeatures_management(self.filepath, outputLocation)
            JoinField_management(outputLocation, "FID", valueToPoint, "FID", "RASTERVALU")
            addProperty = utils.makeObject(outputLocation)
            Delete_management(polyToPoint)
            Delete_management(valueToPoint)
            #TODO implement method that the parameters "CENTROID" or "INSIDE" for FeatureToPoint_management() can be selected

        else:
            raise NotImplementedError("unknown shapeType:", desc.shapeType)

        # update cc instance's attributes
        desc = Describe(outputLocation)
        addProperty.domain = desc.extent
        addProperty.filepath = outputLocation
        addProperty.filename = os.path.basename(outputLocation)

        return addProperty

    def withProperty(self, sql):
        """
        :param sql: sql expression
        :returns: feature that meets the properties of the sql expression
        """

        name = "wProp_" + str(self.sObj)
        outputLocation = "in_memory\\" + name

        selByAtt = SelectLayerByAttribute_management(self.filepath, "NEW_SELECTION", sql)
        CopyFeatures_management(selByAtt, outputLocation)
        wProp = utils.makeObject(outputLocation)

        # update cc instance's attributes
        desc = Describe(outputLocation)
        wProp.domain = desc.extent
        wProp.filepath = outputLocation
        wProp.filename = os.path.basename(outputLocation)

        return wProp

    """
        helper methods
    """

    def save(self, Output_Folder, Output_Name, extension):
        outputLocation = Output_Folder + "\\" + Output_Name + extension
        CopyFeatures_management(self.filepath, outputLocation)

    def show(self):
        print("\n")
        print("show 5 first table rows for file:", '\x1b[1;36m' + self.filepath + '\x1b[0m') #ainsi colors

        list = []
        fields = ListFields(self.filepath)
        for field in fields:
            list.append(field.name)

        list.remove("Shape")
        header = []
        for field in list:
            header.append(str('{:_^20}'.format(field)))
        print(header)

        count = 1
        with SearchCursor(self.filepath, list) as cursor:

            line = []
            for row in cursor:
                for col in row:
                    line.append(str('{:^20}'.format(col)))
                print(line)
                line = []
                if count >= 5:
                    break
                count += 1

        del cursor