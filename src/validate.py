import pandas as pd
import logging

logging.getLogger(__name__)

def validate_data(df: pd.DataFrame, required_columns: list):
    """
    Valida que el dataframe contenga las columnas requeridas y que no tenga valores nulos en esas columnas.
    Args:
        df (pd.DataFrame): DataFrame a validar.
        required_columns (list): Lista de columnas que deben estar presentes y no contener nulos.
    """
    #Extraer las columnas ahora
    columnas_ahora = list(df.columns)
    #verificar las columnas faltantes
    columnas_perdidas = [col for col in required_columns if col not in columnas_ahora]
    if columnas_perdidas:
        raise ValueError(f"Faltan columnas requeridas: {columnas_perdidas}")
    #Advertir si hay valores nulos
    if df.isnull().any().any():
        logging.warning("El DataFrame contiene valores nulos en las columnas requeridas.")