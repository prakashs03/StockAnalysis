import pandas as pd
from sqlalchemy import create_engine

#  Load Excel files instead of CSVs
stock_df = pd.read_csv("final_stock_data.csv")
merged_df = pd.read_csv("final_merged_data.csv")
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# PostgreSQL connection details
user = 'postgres'  # Your username
password = 'root'  # Your Password
host = 'localhost'
port = '5432'
database = 'stock_analysis'# Your Database name

# SQLAlchemy engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

#  Upload DataFrames to PostgreSQL
stock_df.to_sql('stock_data', engine, index=False, if_exists='replace')
sector_df.to_sql('sector_data', engine, index=False, if_exists='replace')
merged_df.to_sql('merged_data', engine, index=False, if_exists='replace')

print(" All files uploaded to PostgreSQL successfully.")
