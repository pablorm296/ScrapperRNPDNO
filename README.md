# RNPDNO Scrapper

This repository contains a Python-based scrapper to extract information from the [public version of Mexico's National Registry of Missing and Untraceable Persons](https://versionpublicarnpdno.segob.gob.mx). The main objective is to create a database of all the missing and untraceable persons in Mexico at neighborhood (_colonia_) level.

## About the RNPDNO

Mexico's National Registry of Missing and Untraceable Persons (Registro Nacional de Personas Desaparecidas y No Localizadas, RNPDNO by its acronym in Spanish) is a centralized database that gathers information of missing and untraceable persons in Mexico. 

The National Search Commission (Comisión Nacional de Búsqueda, CNB by its acronym in Spanish) is in charge of maintaining the RNPDNO. The CNB is a government agency subordinated to Mexico's Ministry of the Interior (Secretaría de Gobernación).

The RNPDNO is mainly fed from the information gathered by each state's Attorney Office and the (Federal) Attorney General's Office. Plus, the CNB has a [public web app](https://cnbreportadesaparecidos.segob.gob.mx) where users can file a missing or uncontactable person report. 

The RNPDNO was created in 2017 after the Mexican Congress had passed [a law](http://www.diputados.gob.mx/LeyesBiblio/pdf/LGMDFP_200521.pdf) that created multiple agencies whose main objective is to search for missing and untraceable persons, as well as preventing, prosecuting, and registering forced disappearance cases. This agencies coordinate the federal and local governments on this efforts.

## Why this scrapper?

The RNPDNO has a public version hosted in a [public web app](https://versionpublicarnpdno.segob.gob.mx). In the public version of the RNPDNO, users can visualize a general summary on the number of missing and untraceable persons in Mexico. Users can also get general summaries at the county (_municipio_) and neighborhood (_colonia_) level. 

The public version of the RNPDNO has three main problems that hinder the use of this information in research projects. First, **the information available at the public version of the RNPDNO is only presented in charts** (bar, line, and area charts). Secondly, **users can only query information from one state, county or neighborhood at a time**. Finally, **there aren't any tools available for exporting in an open format the queried data**.

## License

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/pablorm296/ScrapperRNPDNO">RNPDNO Scrapper</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/pablorm296/">Pablo Reyes Moctezuma</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p> 

This means that:

1. You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
2. You may not use the material for commercial purposes. 
3. If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original. 
4. You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

This is a human-readable summary of (and not a substitute for) the license. The legal code of the license is available at the LICENSE file in the root directory of this repository.