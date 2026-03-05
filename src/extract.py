import pandas as pd
import os
from src.config import DATA_PATH
import logging

# Configuración de logging
logging.getLogger(__name__)

def extract_data():
    """
    Extrae datos desde archivos CSV y los carga en un diccionario de DataFrames.

    Returns:
        dict: Diccionario con los nombres de las tablas como claves y DataFrames como valores.
    """
    tables = {}
    files = {
        'departments': 'rrhh_departments.csv',
        'employees': 'rrhh_employees.csv',
        'salaries': 'rrhh_salaries.csv',
    }

    for table, filename in files.items():
        file_path = os.path.join(DATA_PATH, filename)
        if os.path.exists(file_path):
            tables[table] = pd.read_csv(file_path)
            logging.info(f"{table}: {len(tables[table])} records extracted.")
        else:
            logging.warning(f"File {filename} not found in {DATA_PATH}.")
    return tables