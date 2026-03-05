import pandas as pd
from src.database import get_db_connection, create_table, load_data_to_table
from src.config import DB_CONFIG
import logging

logging.getLogger(__name__)

def load_data_topostgres(df_employees_clean: pd.DataFrame, df_departments_clean: pd.DataFrame, df_salaries_clean: pd.DataFrame):
    logging.info("Cargando datos a PostgreSQL...")
    dtype_mapping = {
        'int64': 'INT',
        'float64': 'DOUBLE PRECISION',
        'object': 'TEXT',
        'datetime64[ns]': 'TIMESTAMP',
        'bool': 'BOOLEAN'
    }
    primary_keys = {
        "employees": "employee_id",
        "departments": "department_id",
        "salaries": "salary_id"
    }
    foreign_keys = {
        "employees": {
            "department_id": ("departments", "department_id"),
        },
        "salaries": {
            "employee_id": ("employees", "employee_id")
        }
    }

    # Usar el administrador de contexto para manejar la conexión y el cursor
    with get_db_connection(DB_CONFIG) as conn:
        cursor = conn.cursor()
        for df, table_name in zip([df_departments_clean, df_employees_clean, df_salaries_clean], ['departments', 'employees', 'salaries']):
            columns = []
            for col, dtype in df.dtypes.items():
                pg_dtype = dtype_mapping.get(str(dtype), 'TEXT')
                column_def = f"{col} {pg_dtype}"
                if col == primary_keys[table_name]:
                    column_def += " PRIMARY KEY"
                columns.append(column_def)

            # Crear la tabla y cargar los datos
            create_table(cursor, table_name, columns, foreign_keys=foreign_keys.get(table_name))
            load_data_to_table(cursor, df, table_name)

        conn.commit()
    logging.info("Datos cargados exitosamente.")
    return True