# Replication of the Question based Spatial Computing Approach

Abstract: A Python implementation of the core concepts of spatial information from Kuhn, Ballatore, Ahlgren, Thiemann, Zimmer, Vahedi, Hervey, Lafia and Jiang (2018) on a case study, the urban water analysis (ICRC, 2017).

See the [Readme] https://github.com/spatial-ucsb/ConceptsOfSpatialInformation/blob/master/README.md of the original repository for general information about the Core Concepts.

The implementation is a development of the original repository that is in a proof of concept state. It still should not be considered stable for a production environment.

Contents
-----------------------------
spatial analyses:
- `UrbanWater.py`: Conventinal spatial analysis.
- `UrbanWater_cc.py`: Spatial analysis with the core concepts.

core concepts library:
- `coreconcepts.py`: Abstract concepts.
- `fields.py`: Implementations of fields.
- `objects.py`: Implementations of objects.
- `utils.py`: Utilities.


References:
- ICRC (International Committee of the Red Cross), 2017	Calculating Buildings Being Supplied by a Water Point. Draft tutorial about Urban Water Toolbox, Geneva, Switzerland.

- Kuhn, Werner, Andrea Ballatore, Eric Ahlgren, MarcThiemann, Michel Zimmer, Behazd Vahedi, Thomas Hervey, Sara Lafia, Liangcun Jiang, 2018[2014]	Specifications and Resources towards a Language for Spatial Computing: Spatial-Ucsb/ConceptsOfSpatialInformation. Haskell, JavaScript, Python, RDF. spatial@ucsb. https://github.com/spatial-ucsb/ConceptsOfSpatialInformation, accessed September 26, 2018.
