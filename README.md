# RNPDNO Scrapper

**(EN)**

This repository contains a Python-based scrapper to extract information from the [public version of Mexico's National Registry of Missing and Untraceable Persons](https://versionpublicarnpdno.segob.gob.mx). The main objective is to create a database of all the missing and untraceable persons in Mexico at neighborhood (_colonia_) level.

**(ES)**

Este repositorio contiene un _scrapper_ escrito en Python para extraer información de la [Versión Pública del Registro Nacional de Personas Desaparecidas y No Localizadas](https://versionpublicarnpdno.segob.gob.mx). El principal objetivo de este _scrapper_ es crear una base de datos —a nivel colonia— de los casos de personas desaparecidas y no localizables en México.

## Español

### ¿Qué es el RNPDNO?

El Registro Nacional de Personas Desaparecidas y No Localizadas (RNPDNO) es un registro centralizado de los casos de personas desaparecidas y no localizadas en México. Se entiende por persona desaparecida como aquella cuyo  paradero  se  desconoce  y  se  presume,  a  partir  de cualquier indicio, que su ausencia se relaciona con la comisión de un delito. Una persona no localizable es aqulla cuya ubicación se desconoce y, que de acuerdo con la información que se reporte a la autoridad, su ausencia no se relaciona con la probable comisión de algún delito.

La Comisión Nacional de Búsqueda (CNB) es el órgano encargado de mantener y administrar el RNPDNO. La CNB es una órgano desconcentrado de la Secretaría de Gobernación (es decir, subordinado jerárquico y **sin** personalidad jurídina ni patrimonio propio) cuyo mandato es determinar, ejecutar y dar seguimiento a las  acciones  de búsqueda  de personas desaparecidas y no localizadas en México.

El RNPDNO se alimenta, principalmente, de la información proporcionada por la Fiscalía General de la República (FGR) y las fiscalías de las 32 entidades federativas. Adicionalmente, la CNB cuenta con una [aplicación web pública](https://cnbreportadesaparecidos.segob.gob.mx) donde cualquier usuario puede hacer un reporte de persona desaparecida o no localizada.

El RNPDNO nació en 2017, después de la aprobación de la [_Ley General en Materia de Desaparición Forzada de Personas_](http://www.diputados.gob.mx/LeyesBiblio/pdf/LGMDFP_200521.pdf), y sustituyó al extinto Registro Nacional de Personas Extraviadas o Desaparecidas. Además, esta ley creó mecanismos de coordinación entre los distintos niveles de govierno para prevenir, perseguir y registrar los casos de desaparición forzada.

### ¿Por qué un scrapper?

El RNPDNO cuenta con una versión pública [disponible para conuslta desde una aplicación web](https://versionpublicarnpdno.segob.gob.mx). En la versión pública del RNPDNO, los usuarios pueden consultar un resumen general sobre el estado de personas desaparecidas y no localizadas en México. Este resumen puede ser desglozado a nivel nacional, estatal, municipal o por colonia.

Sin embargo, la versión pública del RNPDNO tiene tres principales problemas. En primer lugar, **la información disponible sólo se presenta por medio de gráficos** (de barra, línea y área) que carecen de herramientas interactivas, tienen una pobre elección de tipografía y paleta de colores, entre otros problemas. Esto dificulta la consulta de la información. En segundo lugar, los usuarios **sólo pueden consultar la información de un estado, municipio o colonia a la vez**, entorpeciendo las comparaciones entre unidades geográficas. Finalmente, los usuarios **no cuentan con herramientas para exportar los datos consultados en formatos de datos abiertos**. 

Investigadores, en la academia y organizaciones de la sociedad civil, necesitan acceso a estos datos para **profundizar nuestro conocimiento sobre el problema de la desaparición forzada de personas y, en general, la violencia e inseguridad en nuestro país.** Las investigaciones en estas áreas pueden generar recomendaciones de política pública para distribuir de mejor manera los recursos políticos y presupuestarios para atender esta problemática. Adicionalmente, el acceso a estos datos permitirá a actores académicos y de la sociedad civil a **realizar un monitoreo independiente del RNPDNO y las acciones del gobierno para buscar a personas desaparecidas**, así como para contrastar la información con otras fuentes. 

Hasta julio de 2021, la Secretaría de Gobernación se ha negado a compartir versiones abiertas de los datos contenidos en el RNPDNO, a pesar que El Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI) se lo ha pedido en, al menos, tres ocasiones.

### Licencia

Copyright © 2021 Pablo Reyes Moctezuma.

RNPDNO Scrapper se distribuye bajo una licencia _GNU General Public License v3.0_. 

RNPDNO Scrapper es un _software_ libre y gratuito, por lo que no incluye garanría alguna. Puedes redistribuir este software y hacerle modificaciones, bajo ciertas condiciones. Por favor, véase la licencia en el archivo LICENSE de este repositorio.

## English

### About the RNPDNO

Mexico's National Registry of Missing and Untraceable Persons (Registro Nacional de Personas Desaparecidas y No Localizadas, RNPDNO by its acronym in Spanish) is a centralized database that gathers information of missing and untraceable persons in Mexico. 

The National Search Commission (Comisión Nacional de Búsqueda, CNB by its acronym in Spanish) is in charge of maintaining the RNPDNO. The CNB is a government agency subordinated to Mexico's Ministry of the Interior (Secretaría de Gobernación).

The RNPDNO is mainly fed from the information gathered by each state's Attorney Office and the (Federal) Attorney General's Office. Plus, the CNB has a [public web app](https://cnbreportadesaparecidos.segob.gob.mx) where users can file a missing or uncontactable person report. 

The RNPDNO was created in 2017 after the Mexican Congress had passed [a law](http://www.diputados.gob.mx/LeyesBiblio/pdf/LGMDFP_200521.pdf) that created multiple agencies whose main objective is to search for missing and untraceable persons, as well as preventing, prosecuting, and registering forced disappearance cases. These agencies coordinate the federal and local governments on this efforts.

### Why this scrapper?

The RNPDNO has a public version hosted in a [public web app](https://versionpublicarnpdno.segob.gob.mx). In the public version of the RNPDNO, users can visualize a general summary on the number of missing and untraceable persons in Mexico. Users can also get general summaries at the county (_municipio_) and neighborhood (_colonia_) level. 

The public version of the RNPDNO has three main problems that hinder the use of this information in research projects. First, **the information available at the public version of the RNPDNO is only presented in charts** (bar, line, and area charts). Secondly, **users can only query information from one state, county or neighborhood at a time**. Finally, **there aren't any tools available for exporting in an open format the queried data**.

Researchers in academia and civil society need this data to **better understand forced disappearances in Mexico and, in general, geographic patterns of insecurity**. Primarily, this will allow to get public-policy recommendations on how to better allocate resources to address this problems. Additionally, this data can allow researchers to **independently monitor government efforts to register and search for missing persons**.

As of July 2021, the Ministry of Interior or the CNB haven't released open format versions of the database in the RNPDNO. Even when the National Institute of Transparency and Access to Public Information has requested to release the full database in at least three occasions.

### License

Copyright © 2021 Pablo Reyes Moctezuma.

RNPDNO Scrapper is distributed under the _GNU General Public License v3.0_. 

RNPDNO Scrapper is free software and comes with ABSOLUTELY NO WARRANTY. You are welcome to redistribute it under certain conditions.

Please refer to the LICENSE file at the root directory of this repository.
