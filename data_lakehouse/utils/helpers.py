from pandas import DataFrame
from config.constants import VALID_ROUTES
import os

def save_on_data_lake(route: str, df: DataFrame, dataset_name: str):

    if route not in VALID_ROUTES:
        raise ValueError(f"Layer not valid: {route}")

    os.makedirs(f"{route}", exist_ok=True)

    parquet_route = str(f"{route}/{dataset_name}")
    df.to_parquet(parquet_route, index=False, engine="pyarrow")
