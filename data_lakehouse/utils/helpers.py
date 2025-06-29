from pandas import DataFrame
from numpy import nan
from config.constants import VALID_ROUTES
import os

def save_on_data_lake(route: str, df: DataFrame, dataset_name: str):

    if route not in VALID_ROUTES:
        raise ValueError(f"Layer not valid: {route}")

    os.makedirs(f"{route}", exist_ok=True)

    parquet_route = str(f"{route}/{dataset_name}")
    df.to_parquet(parquet_route, index=False, engine="pyarrow")
    
# Función para remplazar vacios por verdaderos nulos
def replace_null_values(dataframe: DataFrame):
    null_values = ['None', 'N/A', 'NA', '', ' ', 'null', 'nan']
    # Se usa el inplace para modificar el dataframe original
    return dataframe.replace(null_values, nan, inplace=True)

# Devuelve la cantidad de valores nan por columna
def verified_nan_values(dataFrame: DataFrame):
    columns = dataFrame.columns
    for column in columns:
        nan_qt = dataFrame[column].isna().sum()
        print(f'Cantidad de valores NaN en {column}: {nan_qt}')