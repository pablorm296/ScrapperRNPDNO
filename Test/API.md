# Public version of the RNPDNO

---

- [Public version of the RNPDNO](#public-version-of-the-rnpdno)
  - [Fechas](#fechas)
  - [Catálogo API](#catálogo-api)
    - [Host](#host)
    - [Root](#root)
    - [Endpoints](#endpoints)
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

#### Municipios

**Description**: Returns a list of objects containing the name and ID of municipalities. The field `Value` contains the municipality ID, and the field `Value` contains the municipality name.

**Request body type**: JSON

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

**Description**: Returns a list of objects containing the name and id of all neighborhoods in the requested municipality. The field `Value` contains the neighborhood ID, and the field `Value` contains the neighborhood name.

**Request body type**: JSON

**Request body**:

```json
{
    "idEstado": "string",
    "idMunicipio": "string"
}
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
