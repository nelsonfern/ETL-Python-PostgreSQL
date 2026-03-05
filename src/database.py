
import psycopg2
from contextlib import contextmanager
from io import StringIO
from src.config import DB_CONFIG

# Función para obtener la conexión a la base de datos
@contextmanager
def get_db_connection(config):
    conn = psycopg2.connect(**config)
    try:
        yield conn
    finally:
        conn.close()

# Función para crear tablas
def create_table(cursor, table_name, columns, foreign_keys=None):
    fk_constraints = []
    if foreign_keys:
        for col, (ref_table, ref_col) in foreign_keys.items():
            fk_constraints.append(f"FOREIGN KEY ({col}) REFERENCES {ref_table}({ref_col})")
    
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(columns + fk_constraints)}
    )
    """
    cursor.execute(create_table_query)

# Función para cargar datos
def load_data_to_table(cursor, df, table_name):
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)
    cursor.copy_from(buffer, table_name, sep=',')