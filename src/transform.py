import pandas as pd
import logging

logging.getLogger(__name__)

def transform_data(tables: dict) -> pd.DataFrame:
    logging.info("Transformando datos...")
    
    df_departments = tables['departments'].copy()
    df_employees = tables['employees'].copy()
    df_salaries = tables['salaries'].copy()

    # Limpieza de datos
    df_employees_clean = df_employees.dropna(subset=['employee_id', 'department_id'])
    df_employees_clean['manager_id'] = df_employees_clean['manager_id'].fillna(0).astype(int)

    df_departments_clean = df_departments.dropna(subset=['department_id'])
    df_departments_clean['location'] = df_departments_clean['location'].fillna('Unknown')

    df_salaries_clean = df_salaries.dropna(subset=['salary_id', 'employee_id', 'base_salary'])
    df_salaries_clean['bonus_percentage'] = df_salaries_clean['bonus_percentage'].fillna(0)

    # Transformación de datos
    df_employees_clean['birth_date'] = pd.to_datetime(df_employees_clean['birth_date'], errors='coerce')
    df_employees_clean['hire_date'] = pd.to_datetime(df_employees_clean['hire_date'], errors='coerce')
    df_employees_clean['age'] = (pd.Timestamp.now() - df_employees_clean['birth_date']).dt.days // 365
    df_employees_clean['is_manager'] = df_employees_clean['employee_id'].isin(df_employees_clean['manager_id'])

    df_departments_clean['created_at'] = pd.to_datetime(df_departments_clean['created_at'], errors='coerce')
    df_salaries_clean['base_salary'] = df_salaries_clean['base_salary'].astype(float)
    df_salaries_clean['effective_date'] = pd.to_datetime(df_salaries_clean['effective_date'], errors='coerce')

    logging.info(f"Registros después de limpieza: Employees={len(df_employees_clean)}, Departments={len(df_departments_clean)}, Salaries={len(df_salaries_clean)}")
    
    return df_employees_clean, df_departments_clean, df_salaries_clean