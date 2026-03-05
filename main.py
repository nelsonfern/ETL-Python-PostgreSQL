from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data_topostgres
from src.validate import validate_data
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting ETL pipeline...")
        # Extract
        tables = extract_data()
        # Transform
        df_employees_clean, df_departments_clean, df_salaries_clean = transform_data(tables)
        validate_data(df_employees_clean, list(df_employees_clean.columns))
        validate_data(df_departments_clean, list(df_departments_clean.columns))
        validate_data(df_salaries_clean, list(df_salaries_clean.columns))
        # Load
        load_data_topostgres(df_employees_clean, df_departments_clean, df_salaries_clean)
        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Error in ETL pipeline: {e}")
        raise

if __name__ == "__main__":
    main()