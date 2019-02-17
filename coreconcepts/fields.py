""""----------------------------------------------------------------------------
Name:         fields.py
Purpose:      coreconcepts library
Project:      language for spatial computing
Author:       Kuhn et al. 2018, adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    os, coreconcepts, arcpy -----------"""

import os
from coreconcepts.coreconcepts import CcField
from coreconcepts import utils
from arcpy import Describe, CopyRaster_management
from arcpy.sa import ExtractByMask

class GeoTiffField(CcField):
    """
    Concrete class for core concept 'field'
    For handling .tif files
    """
    def __init__(self, filepath, objIndex, domain):
        super().__init__(filepath, objIndex, domain)
        self.filepath = filepath
        self.sObj = objIndex
        self.domain = domain
        self.filename = os.path.basename(filepath)

    def restrictDomain(self, object, operation):
        """
        Restricts current instance's domain based on object's domain
        @param object: extent to which the field is restricted
        @param operation: valid options: "inside", "outside"
        """

        if operation == 'inside':

            name = "restDom_in_" + str(self.sObj)
            outputLocation = "in_memory\\" + name + ".tif"

            # extract by mask
            outRaster = ExtractByMask(self.filepath, object.filepath)
            CopyRaster_management(outRaster, outputLocation)
            restDom = utils.makeField(outputLocation)

        elif operation == 'outside':
            raise NotImplementedError("restrictDomain 'outside'")

        else:
            raise NotImplementedError(operation)

        # update cc instance's attributes
        desc = Describe(outputLocation)
        restDom.filepath = outputLocation
        restDom.domain = desc.extent
        restDom.filename = os.path.basename(outputLocation)

        return restDom

    def local(self, fields, operation):
        raise NotImplementedError("getValue")

    def coarsen(self, cellW, cellH):
        raise NotImplementedError("getValue")

    def getValue(self, pos):
        raise NotImplementedError("getValue")

    def domain(self):
        return self.domain

    """
    helper methods
    """

    def save (self, Output_Folder, Output_Name, extension):
        outputLocation = Output_Folder + "\\" + Output_Name + extension
        print("saved to", outputLocation)
        CopyRaster_management(self.filepath, outputLocation)