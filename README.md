# Replication of the Question based Spatial Computing Approach

*Abstract:* A Python implementation of the core concepts of spatial information from Kuhn, Ballatore, Ahlgren, Thiemann, Zimmer, Vahedi, Hervey, Lafia and Jiang (2018) on a case study, the urban water analysis (ICRC, 2017).

*Keywords:* language for spatial computing; question-based analysis; domain-specific language; transdisciplinarity

See the [Readme] https://github.com/spatial-ucsb/ConceptsOfSpatialInformation/blob/master/README.md of the original repository for general information about the Core Concepts.

The implementation is a development of the original repository that is in a proof of concept state. It still should not be considered stable for a production environment.

Contents
-----------------------------
- [spatial analyses](CaseStudy): Conventional analysis and spatial analysis with the core concepts of the case study.
- `UrbanWater.py`: Conventinal spatial analysis.
- `UrbanWater_cc.py`: Spatial analysis with the core concepts.

core concepts library:
- `coreconcepts.py`: Abstract concepts.
- `fields.py`: Implementations of fields.
- `objects.py`: Implementations of objects.
- `utils.py`: Utilities.


References
-----------------------------
- Allen, C., Hervey, T., Lafia, S., Phillips, D., Vahedi, B., Kuhn, W. (2016). *Exploring the Notion of Spatial Data Lenses.* Geographic Information Science, 9927, 259-274. <[PDF](http://link.springer.com/10.1007/978-3-319-45738-3_17)>
- ICRC (International Committee of the Red Cross), 2017	Calculating Buildings Being Supplied by a Water Point. Draft tutorial about Urban Water Toolbox, Geneva, Switzerland.
- Kuhn, Werner, Andrea Ballatore, Eric Ahlgren, MarcThiemann, Michel Zimmer, Behazd Vahedi, Thomas Hervey, Sara Lafia, Liangcun Jiang, 2018[2014]	Specifications and Resources towards a Language for Spatial Computing: Spatial-Ucsb/ConceptsOfSpatialInformation. Haskell, JavaScript, Python, RDF. spatial@ucsb. https://github.com/spatial-ucsb/ConceptsOfSpatialInformation, accessed September 26, 2018.
- Kuhn, W. & Ballatore, A. (2015). *Designing a Language for Spatial Computing.* Lecture Notes in Geoinformation and Cartography 2015, AGILE, Lisbon, Portugal, pp 309-326. Best Paper Award. <[PDF](http://escholarship.org/uc/item/04q9q6wm)>
- Kuhn, W. (2012). *Core concepts of spatial information for transdisciplinary research.* International Journal of Geographical Information Science, 26(12), 2267-2276. <[PDF](http://ifgi.uni-muenster.de/~kuhn/research/publications/pdfs/refereed%20journals/IJGIS%202012.pdf)>
- Vahedi, B., Kuhn, W., Ballatore A. (2016). *Question-Based Spatial Computing - A Case Study.* In T. Sarjakoski, M. Y. Santos, & L. T. Sarjakoski (Eds.), Lecture Notes in Geoinformation and Cartography (AGILE 2016) (pp. 37 - 50). Berlin: Springer. <[PDF](https://link.springer.com/chapter/10.1007/978-3-319-33783-8_3)>
