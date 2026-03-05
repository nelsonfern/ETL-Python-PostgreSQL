# Proyecto ETL: Transformación de Datos desde CSV a PostgreSQL

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para procesar datos almacenados en archivos CSV y cargarlos en una base de datos PostgreSQL. El objetivo es limpiar, transformar y validar los datos antes de almacenarlos en tablas relacionales. Fue creado a modo de experimentar / poner en practica conocimientos adquiridos durante cursos y bootcamps que he estado tomando. 

---

## Estructura del Proyecto
El proyecto está organizado en los siguientes módulos:

- **`main.py`**: Orquesta el pipeline ETL llamando a las funciones de extracción, transformación, validación y carga.
- **`src/extract.py`**: Contiene la lógica para extraer datos desde archivos CSV.
- **`src/transform.py`**: Realiza la limpieza y transformación de los datos.
- **`src/validate.py`**: Valida que los datos cumplan con los requisitos antes de cargarlos.
- **`src/load.py`**: Carga los datos transformados en la base de datos PostgreSQL.
- **`src/database.py`**: Maneja la conexión a la base de datos y la creación de tablas.
- **`src/config.py`**: Contiene configuraciones como las credenciales de la base de datos y las rutas de los archivos.

---

## Requisitos

### Dependencias
- Python 3.8 o superior
- PostgreSQL
- Paquetes de Python:
  - `pandas`
  - `psycopg2`
  - `python-dotenv`

### Instalación
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```
2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configura las credenciales de la base de datos en un archivo `.env`:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=mi_base_de_datos
   DB_USER=mi_usuario
   DB_PASSWORD=mi_contraseña
   ```

---

## Uso
1. Asegúrate de que los archivos CSV estén en la carpeta `data/`.
2. Ejecuta el pipeline:
   ```bash
   python main.py
   ```
3. Si todo funciona correctamente, los datos se cargarán en la base de datos PostgreSQL.

---

## Flujo del Pipeline

### 1. Extracción (`extract_data`)
- Lee los archivos CSV desde la carpeta `data/`.
- Devuelve un diccionario con los nombres de las tablas como claves y los DataFrames como valores.

### 2. Transformación (`transform_data`)
- Limpia los datos eliminando valores nulos y transformando columnas.
- Calcula nuevas columnas como `age` y `is_manager`.

### 3. Validación (`validate_data`)
- Verifica que los DataFrames contengan las columnas requeridas.
- Emite advertencias si hay valores nulos.

### 4. Carga (`load_data_topostgres`)
- Crea las tablas en PostgreSQL si no existen.
- Inserta los datos transformados en las tablas correspondientes.
- Además, crea las Foreing Keys por lo tanto es una base de datos relacional.

---

## Archivos de Entrada
- Los Dataset usados en este proyecto no estan incluidos pues no son de mi autoria, 
- la estructura esperada seria:
- `data/`:
-   `rrhh_departments.csv`: Información de los departamentos.
-   `rrhh_employees.csv`: Información de los empleados.
-   `rrhh_salaries.csv`: Información de los salarios.

---

## Archivos de Salida
- Los datos se cargan en las siguientes tablas de PostgreSQL:
  - `departments`
  - `employees`
  - `salaries`

---

## Notas
- Asegúrate de que la base de datos PostgreSQL esté en ejecución antes de iniciar el pipeline.
- Si un archivo CSV no se encuentra, el pipeline emitirá una advertencia y continuará con los archivos disponibles.
-
---

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## Autor
- **Fernandez, Nelson Isaias**
- Contacto: [nelsonfern83@gmail.com](mailto:nelsonfern83@gmail.com)