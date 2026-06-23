import pandas as pd
import os

# Path to raw data folder
data_path = "data/raw"

# Get all files inside folder
files = os.listdir(data_path)

print("CSV Files Found:")
for file in files:
    print(file)

print("\n" + "=" * 50)

# Read each CSV file
for file in files:
    if file.endswith(".csv"):
        file_path = os.path.join(data_path, file)

        print(f"\nLoading: {file}")

        df = pd.read_csv(file_path)

        print("Shape:", df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

        print("\n" + "=" * 50)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())
print("\nUnique Categories:")
print(fund_master["category"].unique())
print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())
print("\nUnique Risk Grades:")
print(fund_master["risk_category"].unique())
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nMissing AMFI Codes:")
print(missing_codes)