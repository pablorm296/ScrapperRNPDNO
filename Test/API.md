# Public version of the RNPDNO

---

- [Public version of the RNPDNO](#public-version-of-the-rnpdno)
  - [Fechas](#fechas)
  - [Catálogo API](#catálogo-api)
    - [Host](#host)
    - [Root](#root)
    - [Endpoints](#endpoints)
      - [Estados](#estados)
      - [Municipios](#municipios)
      - [Colonias](#colonias)
  - [Sociodemográficos API](#sociodemográficos-api)
    - [Host](#host-1)
    - [Root](#root-1)
    - [Values](#values)
      - [idEstatusVictima](#idestatusvictima)
      - [idHipotesisNoLocalizacion](#idhipotesisnolocalizacion)
    - [Endpoints](#endpoints-1)
      - [Totales](#totales)
      - [BarChartSexoColonia](#barchartsexocolonia)
      - [AreaChartSexoAnio](#areachartsexoanio)

--- 

## Fechas

**Fecha de inicio**: 15/03/1964

---

## Catálogo API

### Host

`https://versionpublicarnpdno.segob.gob.mx/`

### Root

`/Catalogo/`

### Endpoints

#### Estados

**Description**: Returns a list of objects containing the name and ID of Mexican states. The field `Value` contains the state ID, and the field `Text` contains the state name.

**Request body type**: Form data

**Request body**:

**Response body example**:

```json
[
    {"Value":0,"Text":"--TODOS--"},
    {"Value":1,"Text":"AGUASCALIENTES"}
]
```

#### Municipios

**Description**: Returns a list of objects containing the name and ID of municipalities. The field `Value` contains the municipality ID, and the field `Text` contains the municipality name.

**Request body type**: Form data

**Request body**:

```json
{"idEstado": "string"}
```

**Response body example**:

```json
[
    {"Value":0,"Text":"--TODOS--"},
    {"Value":1,"Text":"ABALÁ"}
]
```

#### Colonias

**Description**: Returns a list of objects containing the name and id of all neighborhoods in the requested municipality. The field `Value` contains the neighborhood ID, and the field `Text` contains the neighborhood name.

**Request body type**: Form data

**Request body**:

```json
{
    "idEstado": "string",
    "idMunicipio": "string"
}
```

**Response body example**:

```json
[
    {"Value":0,"Text":"--TODAS--"},
    {"Value":294045,"Text":"1° DE MAYO"}
]
```

---

## Sociodemográficos API

### Host

`https://versionpublicarnpdno.segob.gob.mx/`

### Root

`/Sociodemograficos/`

### Values

#### idEstatusVictima

```html
<select id="cboEstatus" name="cboEstatus" class="form-control black-options" required="">
    <option value="0" selected="">PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS</option>
    <option value="7">PERSONAS DESAPARECIDAS Y NO LOCALIZADAS</option>
    <option value="4">PERSONAS DESAPARECIDAS</option>
    <option value="5">PERSONAS NO LOCALIZADAS</option>
    <option value="6">PERSONAS LOCALIZADAS</option>
    <option value="2">PERSONAS LOCALIZADAS CON VIDA</option>
    <option value="3">PERSONAS LOCALIZADAS SIN VIDA</option>
</select>
```

#### idHipotesisNoLocalizacion

```html
<select class="form-control black-options" id="cboHipotesis" name="cboHipotesis">
    <option value="0">--TODAS--</option>
    <option value="1">ACCIDENTE</option>
    <option value="2">CATÁSTROFE</option>
    <option value="3">NO LOCALIZACIÓN VOLUNTARIA</option>
    <option value="4">NO LOCALIZACIÓN INVOLUNTARIA</option>
    <option value="5">SE DESCONOCE</option>
</select>
```

### Endpoints

#### Totales

**Description**: Returns an object containing a global summary of the queried data.

**Request body type**: JSON

**Request body**:

```json
{
    "titulo":"PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS",
    "idEstatusVictima":"0",
    "fechaInicio":"",
    "fechaFin":"",
    "idEstado":"9",
    "idMunicipio":"3",
    "mostrarFechaNula":"0",
    "idColonia":"0",
    "idNacionalidad":"0",
    "edadInicio":"",
    "edadFin":"",
    "mostrarEdadNula":"0",
    "idHipotesis":"",
    "idMedioConocimiento":"",
    "idCircunstancia":"",
    "tieneDiscapacidad":"",
    "idTipoDiscapacidad":"0",
    "idEtnia":"0",
    "idLengua":"0",
    "idReligion":"",
    "esMigrante":"",
    "idEstatusMigratorio":"0",
    "esLgbttti":"",
    "esServidorPublico":"",
    "esDefensorDH":"",
    "esPeriodista":"",
    "esSindicalista":"",
    "esONG":"",
    "idHipotesisNoLocalizacion":"0",
    "idDelito":"0"
}
```

**Response body example**:

```json
{
    "TotalGlobal":"556",
    "TotalDesaparecidos":"133",
    "TotalLocalizados":"423",
    "PorcentajeDesaparecidos":"23.92 %",
    "PorcentajeLocalizados":"76.08 %",
    "TotalSoloDesaparecidos":"115",
    "TotalSoloNoLocalizados":"18",
    "PorcentajeSoloDesaparecidos":"86.47 %",
    "PorcentajeSoloNoLocalizados":"13.53 %",
    "TotalLocalizadosCV":"409",
    "TotalLocalizadosSV":"14",
    "PorcentajeLocalizadosCV":"96.69 %",
    "PorcentajeLocalizadosSV":"3.31 %"
}
```

#### BarChartSexoColonia

**Description**: Returns an object containing the number of missing people by sex and neighborhood.

**Request body type**: JSON

**Request body**: 

```json
{
    "titulo":"PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS",
    "subtitulo":"POR COLONIAS - IZTAPALAPA",
    "idEstatusVictima":"0",
    "fechaInicio":"",
    "fechaFin":"",
    "idEstado":"9",
    "idMunicipio":"7",
    "mostrarFechaNula":"0",
    "idColonia":"0",
    "idNacionalidad":"0",
    "edadInicio":"",
    "edadFin":"",
    "mostrarEdadNula":"0",
    "idHipotesis":"",
    "idMedioConocimiento":"",
    "idCircunstancia":"",
    "tieneDiscapacidad":"",
    "idTipoDiscapacidad":"0",
    "idEtnia":"0",
    "idLengua":"0",
    "idReligion":"",
    "esMigrante":"",
    "idEstatusMigratorio":"0",
    "esLgbttti":"",
    "esServidorPublico":"",
    "esDefensorDH":"",
    "esPeriodista":"",
    "esSindicalista":"",
    "esONG":"",
    "idHipotesisNoLocalizacion":"0",
    "idDelito":"0"
}
```

**Response body example**:

```json
{
    "Title":"PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS",
    "Subtitle":"POR COLONIAS - IZTAPALAPA",
    "XAxisCategories":["CHINAMPAC DE JUAREZ","UNIDAD EJÉRCITO CONSTITUCIONALISTA","PLAN DE IGUALA","INSURGENTES","LEYES DE REFORMA 1A SECCIÓN","SAN SIMÓN CULHUACÁN","CUCHILLA DEL MORAL","EJERCITO DE AGUA PRIETA","CENTRAL DE ABASTO","MIRAVALLE","SAN LORENZO","LA POLVORILLA","AMPLIACIÓN RICARDO FLORES MAGÓN","IZTLAHUACÁN","RINCONADA DEL MOLINO","ESTRELLA CULHUACÁN","SANTA MARIA AZTAHUACAN","SANTA BÁRBARA","GRANJAS SAN ANTONIO","BUENAVISTA","UNIDAD VICENTE GUERRERO","SAN ANDRÉS TOMATLÁN","JARDINES DE SAN LORENZO TEZONCO","ACULCO","PUENTE BLANCO","PROGRESISTA","CONSEJO AGRARISTA MEXICANO","LOS REYES CULHUACÁN","SANTIAGO ACAHUALTEPEC","SANTA ISABEL INDUSTRIAL"],
    "XAxisTitle":null,
    "YAxisTitle":"Número de personas",
    "YAxisTooltipValueSuffix":" personas",
    "TooltipText":null,
    "PointStar":null,
    "Series":[
        {"name":"Hombre","data":[4,5,1,1,1,1,0,4,11,4,2,4,1,1,1,0,8,7,2,6,8,1,0,2,5,4,10,5,4,2]},
        {"name":"Mujer","data":[5,3,0,0,5,1,1,7,5,3,0,2,1,2,1,1,8,3,5,12,9,2,1,2,0,3,5,2,5,3]},
        {"name":"Indeterminado","data":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        ],
    "TableValues":[
        {"text":"Hombre","value":"844","porcent":"52.52%"},
        {"text":"Mujer","value":"754","porcent":"46.92%"},
        {"text":"Indeterminado","value":"09","porcent":"0.56%"},
        {"text":"\u003cstrong\u003eTotal\u003c/strong\u003e","value":"1,607","porcent":"100.00%"}
        ],
    "TableTotal":null
}
```

#### AreaChartSexoAnio

**Description**: Returns an object containing the number of missing people by sex and year.

**Request body type**: JSON

**Request body**: 

```json
{
    "titulo":"PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS",
    "subtitulo":"POR AÑO ",
    "idEstatusVictima":"0",
    "fechaInicio":"",
    "fechaFin":"",
    "idEstado":"9",
    "idMunicipio":"7",
    "mostrarFechaNula":"0",
    "idColonia":"0",
    "idNacionalidad":"0",
    "edadInicio":"",
    "edadFin":"",
    "mostrarEdadNula":"0",
    "idHipotesis":"",
    "idMedioConocimiento":"",
    "idCircunstancia":"",
    "tieneDiscapacidad":"",
    "idTipoDiscapacidad":"0",
    "idEtnia":"0",
    "idLengua":"0",
    "idReligion":"",
    "esMigrante":"",
    "idEstatusMigratorio":"0",
    "esLgbttti":"",
    "esServidorPublico":"",
    "esDefensorDH":"",
    "esPeriodista":"",
    "esSindicalista":"",
    "esONG":"",
    "idHipotesisNoLocalizacion":"0",
    "idDelito":"0"
}
```

**Response body example**:

```json
{
    "Title":"PERSONAS DESAPARECIDAS, NO LOCALIZADAS Y LOCALIZADAS",
    "Subtitle":"POR AÑO ",
    "XAxisCategories":["1.CIFRA SIN  AÑO DE REFERENCIA","1986","1989","1998","2005","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"],
    "XAxisTitle":"",
    "YAxisTitle":"Número de personas",
    "YAxisTooltipValueSuffix":" personas",
    "TooltipText":null,
    "PointStar":null,
    "Series":[
        {"name":"Hombre","data":[24,0,1,0,1,0,30,48,51,63,89,12,10,2,5,9,267,162,70]},
        {"name":"Mujer","data":[25,1,0,1,0,1,23,43,59,64,98,6,11,5,6,5,222,155,29]},
        {"name":"Indeterminado","data":[9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    ],
    "TableValues":[
        {"text":"Hombre","value":"844","porcent":"52.52%"},
        {"text":"Mujer","value":"754","porcent":"46.92%"},
        {"text":"Indeterminado","value":"09","porcent":"0.56%"},
        {"text":"\u003cstrong\u003eTotal\u003c/strong\u003e","value":"1,607","porcent":"100.00%"}
    ],
    "TableTotal":null
}
```
