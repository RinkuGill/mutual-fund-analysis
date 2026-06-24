import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned CSV files
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_performance.csv")

# Load into SQLite tables
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

# Verify row counts
print("Rows loaded:")
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))

print("\nDatabase created successfully: bluestock_mf.db")