""""----------------------------------------------------------------------------
Name:         utils.py
Purpose:      coreconcepts library
Project:      language for spatial computing
Author:       Kuhn et al. 2018, adapted by Selina Studer
License:      Apache License 2.0
Created:      26.12.2018
Libraries:    coreconcepts, arcpy -----------"""

# make CcField instance
from coreconcepts.fields import GeoTiffField
from coreconcepts.objects import ArcShpObject
from arcpy import Describe, CopyFeatures_management, SelectLayerByAttribute_management

def makeField(filepath):
    """
    :param filepath: data source file path
    :return: new Ccfield instance
    """
    domain = determine_domain(filepath)

    # determine input file type
    if filepath.endswith(".tif"):
        return GeoTiffField(filepath, id(filepath), domain)
    elif filepath.endswith(".mp3"):
        pass
    assert 0, "Bad shape creation: " + filepath

def makeObject(filepath):
    """
    :param filepath: data source file path
    :return: new Ccobject instance
    """
    domain = determine_domain(filepath)

    # determine input file type
    if filepath.endswith((".shp", "")):             # NOTE:"" for files in_memory or gdb
        return ArcShpObject(filepath, id(filepath), domain)
    elif filepath.endswith(".mp3"):
        pass
    assert 0, "Bad shape creation: " + filepath

def determine_domain(filepath):
    """
    :param filepath: data source filepath
    :return: ArcPy domain extent
    """
    desc = Describe(filepath)
    return desc.extent
