import os

# === Base del proyecto ===
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))  # data_lakehouse/

# === Rutas ===
DATA_LAKE_DIR = os.path.join(PROJECT_ROOT, "data_lake")

CSV_LAYER = "csv"
CSV_ROUTE = os.path.join(DATA_LAKE_DIR, CSV_LAYER)

RAW_LAYER = "raw_data"
RAW_ROUTE = os.path.join(DATA_LAKE_DIR, RAW_LAYER)

CLEANSED_LAYER = "cleansed_data"
CLEANSED_ROUTE = os.path.join(DATA_LAKE_DIR, CLEANSED_LAYER)

CURATED_LAYER = "curated_data"
CURATED_ROUTE = os.path.join(DATA_LAKE_DIR, CURATED_LAYER)

# === Capas válidas ===
VALID_ROUTES = {RAW_ROUTE, CLEANSED_ROUTE, CURATED_ROUTE}

# === Nombres de datasets crudos ===
DATA_CSV = "data.csv"
DIRTY_CAFE_SALES_CSV = "dirty_cafe_sales.csv"
FLIPKART_ECOMMERCE_SAMPLE_CSV = "flipkart_com-ecommerce_sample.csv"
RETAIL_STORE_SALES_CSV = "retail_store_sales.csv"
US_SHEIN_APPLIANCES_CSV = "us-shein-appliances-3987.csv"
WAREHOUSE_AND_RETAIL_SALES_CSV = "warehouse_and_retail_sales.csv"

# === Nombres de datasets crudos ===
DATA_RAW = "data_raw.parquet"
DIRTY_CAFE_SALES_RAW = "dirty_cafe_sales_raw.parquet"
FLIPKART_ECOMMERCE_SAMPLE_RAW = "flipkart_com-ecommerce_sample_raw.parquet"
RETAIL_STORE_SALES_RAW = "retail_store_sales_raw.parquet"
US_SHEIN_APPLIANCES_RAW = "us-shein-appliances-3987_raw.parquet"
WAREHOUSE_AND_RETAIL_SALES_RAW = "warehouse_and_retail_sales_raw.parquet"

# === Nombres de datasets limpios (cleansed) ===
DATA_CLEANSED = "data_cleansed.parquet"
DIRTY_CAFE_SALES_CLEANSED = "dirty_cafe_sales_cleansed.parquet"
FLIPKART_ECOMMERCE_SAMPLE_CLEANSED = "flipkart_com-ecommerce_sample_cleansed.parquet"
RETAIL_STORE_SALES_CLEANSED = "retail_store_sales_cleansed.parquet"
US_SHEIN_APPLIANCES_CLEANSED = "us-shein-appliances-3987_cleansed.parquet"
WAREHOUSE_AND_RETAIL_SALES_CLEANSED = "warehouse_and_retail_sales_cleansed.parquet"

# === Nombres de datasets finales (curated) ===
DATA_CURATED = "data_curated.parquet"
DIRTY_CAFE_SALES_CURATED = "dirty_cafe_sales_curated.parquet"
FLIPKART_ECOMMERCE_SAMPLE_CURATED = "flipkart_com-ecommerce_sample_curated.parquet"
RETAIL_STORE_SALES_CURATED = "retail_store_sales_curated.parquet"
US_SHEIN_APPLIANCES_CURATED = "us-shein-appliances-3987_curated.parquet"
WAREHOUSE_AND_RETAIL_SALES_CURATED = "warehouse_and_retail_sales_curated.parquet"

__all__ = [
    "PROJECT_ROOT",
    "VALID_ROUTES",
    "DATA_LAKE_DIR",
    "CSV_LAYER",
    "CSV_ROUTE",
    "RAW_LAYER",
    "RAW_ROUTE",
    "CLEANSED_LAYER",
    "CLEANSED_ROUTE",
    "CURATED_LAYER",
    "CURATED_ROUTE",
    "DATA_CSV",
    "DIRTY_CAFE_SALES_CSV",
    "FLIPKART_ECOMMERCE_SAMPLE_CSV",
    "RETAIL_STORE_SALES_CSV",
    "US_SHEIN_APPLIANCES_CSV",
    "WAREHOUSE_AND_RETAIL_SALES_CSV",
    "DATA_RAW",
    "DIRTY_CAFE_SALES_RAW",
    "FLIPKART_ECOMMERCE_SAMPLE_RAW",
    "RETAIL_STORE_SALES_RAW",
    "US_SHEIN_APPLIANCES_RAW",
    "WAREHOUSE_AND_RETAIL_SALES_RAW",
    "DATA_CLEANSED",
    "DIRTY_CAFE_SALES_CLEANSED",
    "FLIPKART_ECOMMERCE_SAMPLE_CLEANSED",
    "RETAIL_STORE_SALES_CLEANSED",
    "US_SHEIN_APPLIANCES_CLEANSED",
    "WAREHOUSE_AND_RETAIL_SALES_CLEANSED",
    "DATA_CURATED",
    "DIRTY_CAFE_SALES_CURATED",
    "FLIPKART_ECOMMERCE_SAMPLE_CURATED",
    "RETAIL_STORE_SALES_CURATED",
    "US_SHEIN_APPLIANCES_CURATED",
    "WAREHOUSE_AND_RETAIL_SALES_CURATED",
]
