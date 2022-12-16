# Importing modules
import pandas as pd

# Read police Excel data into pandas ExcelFile
xl = pd.ExcelFile('../data/pfafinalmar22.xls')
# Store sheets as dataframes in dictionary
df_dict = {}
for sheet in xl.sheet_names:
    df_dict[f'{sheet}']= pd.read_excel(xl,sheet_name=sheet)
# Show names of dataframes in df_dict
print(df_dict.keys())
# Inspect df with table of contents
contents = df_dict['Table of Contents']
print(contents.head())
# Replace header of contents with first row
contents_header = contents.iloc[0]
contents.columns = contents_header
contents_updated = contents.iloc[1:]
# Inspect values of table titles in updated contents df
print(contents_updated['Table title'].values)
# Assign dataframes of df_dict to variables
df_year_22 = df_dict['Table P1']
df_jan_to_march_22 = df_dict['Table P1a Jan- Mar 22']
df_year_21_vs_22 = df_dict['Table P2']
df_jan_to_march_21_vs_22 = df_dict['Table P2a Jan - Mar 22']
df_rate_year_22 = df_dict['Table P3']
df_offences_year_22 = df_dict['Table P4 previous']
df_knife_year_22 = df_dict['Table P5 ']
df_knife_jan_to_march_22 = df_dict['Table P6 Jan-Mar']
df_knife_years_11_to_22 = df_dict['Table P7 ']
df_knife_rate_years_21_to_22 = df_dict['Table P8']
df_knife_new_vs_old_reporting = df_dict['Table P9 ']
df_firearm_years_10_to_22 = df_dict['Table P10 ']
df_fraud_year_22 = df_dict['Table P11']
df_antisocial_years_08_to_22 = df_dict['Table P12 ']
df_antisocial_year_22 = df_dict['Table P13 ']