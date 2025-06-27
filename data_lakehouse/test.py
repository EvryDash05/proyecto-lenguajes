import glob
import os
from pandas import read_parquet
from utils import helpers
from config.constants import CURATED_LAYER, DATA_CURATED, DATA_RAW

df = read_parquet('./data_lake/raw_data/flipkart_com-ecommerce_raw.parquet')

print(df.head(10))