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

### Endpoints

#### Totales


