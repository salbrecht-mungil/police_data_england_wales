from dataframe_definition import df_year_22
import pandas as pd
import numpy as np

# Inspecting the table and its contents with print(df_year_22.head(10)) -> first 5 rows do not contain data and can be removed
# Delete first 5 rows and reassign header
df_year_22_header = df_year_22.iloc[5]
df_year_22.columns = df_year_22_header
df_year_22_updated = df_year_22.iloc[6:]
# Reset index
df_year_22_updated = df_year_22_updated.reset_index()
# Check shape with print(df_year_22_updated.shape) -> table has 56 rows and 25 columns 
# Check df_year_22_updated with print(df_year_22_updated.info()) -> all dtypes are objects, Area Code has only 55 rows
# Check 'Area Code' for null values with print(df_year_22_updated['Area Code']) -> row 55 has value 'NaN'
# Change all dtypes to int except for 'Area Code' and 'Area Name'
for column in df_year_22_updated:
  if column == 'Area Code' or column == 'Area Name':
    df_year_22_updated[column] = df_year_22_updated[column].astype(str)
  else:
    df_year_22_updated[column] = df_year_22_updated[column].astype(int)
# Replace all NaN with np.nan
df_year_22_updated = df_year_22_updated.replace('NaN', np.nan)
# Check if column names need to be changed with print(df_year_22_updated.keys())
# Change table name for ' Total recorded crime\n (excluding fraud) [note 2]'
df_year_22_updated.rename(columns={' Total recorded crime\n (excluding fraud) [note 2]': 'Total crime excluding fraud'}, inplace=True)