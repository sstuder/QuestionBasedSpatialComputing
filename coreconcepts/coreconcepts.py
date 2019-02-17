""""----------------------------------------------------------------------------
Name:         coreconcepts.py
Purpose:      coreconcepts library
Project:      language for spatial computing
Author:       Kuhn et al. 2018, adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    arcpy -----------"""

from arcpy import CheckOutExtension, env

env.overwriteOutput = True

# Check out any necessary licenses
CheckOutExtension("spatial")

class CcField(object):
    """
    Abstract class for core concept 'field'
    """
    def __init__(self, filepath, objIndex, domain):
        """
        :param filepath: data file path
        :param objIndex: unique ID
        :param domain: desc.extent of the geo_object
        """
        self.filepath = filepath
        self.sObj = objIndex
        self.domain = domain

class CcObject(object):
    """
    Abstract class for core concept 'object'
    """
    def __init__(self, filepath, objIndex, domain):
        """
        :param filepath: data file path
        :param objIndex: unique ID
        :param domain: desc.extent of the geo_object
        """
        self.filepath = filepath
        self.sObj = objIndex
        self.domain = domain