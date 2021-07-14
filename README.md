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

RNPDNO scrapper is distributed under the _GNU General Public License v3.0_. 

Please refer to the LICENSE file at the root directory of this repository.
