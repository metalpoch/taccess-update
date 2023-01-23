# taccess-update
#### Crea ficheros JSON a partir de CSV, además de poder enviarlos mediante el método POST de HTTP
##### Una simple aplicación CLI creada con Python 3.10.6

## Características
- Transforma los reportes CSV en JSON con una estructura elegante para el análisis de datos
- Actualiza tus bases de datos utilizando el método POST del protocolo HTTP
- Muestra en tiempo real desde la terminal el estatus de las operaciones
- Almacena los errores de la operación en un fichero JSON

## Tecnologías
Este CLI utiliza las siguientes dependencias open source para funcionar correctamente:
- [Requests] - Una biblioteca HTTP simple pero elegante
- [Pandas] - Una biblioteca que proporciona estructuras de datos rápidas, flexibles y expresivas diseñadas para que trabajar con datos "relacionales" o "etiquetados" sea fácil e intuitivo
 
## Instalación
##### Clona este repositorio desde [GitHub]
```bash
git clone https://github.com/metalpoch/taccess-update.git
cd taccess-update/
```

##### Crea un entorno virtual
```Bash
virtualenv venv
source venv/bin/activate
```

##### Utiliza [pip] para instalar las dependencias
```bash
pip install -r requirements.txt
```

## Archivo de configuración
Para el funcionamiento de este programa, se necesita que las rutas donde se almacenan los CSV y su estructura estén almacenadas en un fichero "config.json" en el directorio raíz de [taccess-update].

Dentro de la estructura de [config.json]
- LAYER: objetos con la ruta de los reportes y su estructura. Estos reportes se llaman con la bandera **--layer** del CLI
- BLACKLIST: este objeto contiene una lista de cadena de texto. Los reportes que contengan esas cadenas se ignoraran
- API_ACCESS_TOKEN: autenticación, identifican del usuario a la API
- API_ENDPOINTS: es la dirección a la que se enviaran las peticiones. Estas se llaman con la bandera **--update** del CLI

## Listo!
```bash
python main.py --help  # mensaje de ayuda
```

### Ejemplos
##### Convertir los reportes CSV a JSON hacia una ruta temporal: 
```bash
python main.py --layer bras --firstday 20230101 --lastday 20230119 --output tmp/
```
##### Convertir los reportes CSV a JSON hacia una ruta temporal y enviar los datos mediante el protocolo HTTP con el método POST: 
```bash
python main.py --layer bras --firstday 20230101 --lastday 20230119 --output tmp/ --update dashboardTrend
```

Nota:
Las fechas deben estar en formato %Y%m%d ó YYYYMMDD para funcionar correctamente.

[//]: #
   [Pandas]: <https://pandas.pydata.org/docs/index.html>
   [Requests]: <https://pypi.org/project/requests/>
   [pip]: <https://pip.pypa.io/en/stable/>
   [GitHub]: <https://github.com/metalpoch>
   [taccess-update]: <https://github.com/metalpoch/taccess-update>
   [config.json]: <https://github.com/metalpoch/taccess-update/blob/main/config.json>
