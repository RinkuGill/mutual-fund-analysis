import pandas as pd

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

nav_history["date"] = pd.to_datetime(nav_history["date"])
nav_history = nav_history.sort_values(by=["amfi_code", "date"])

#print("\nMissing NAV values:")
#print(nav_history["nav"].isnull().sum())
nav_history["nav"] = nav_history.groupby("amfi_code")["nav"].ffill()
#print("\nDuplicate rows:")
#print(nav_history.duplicated().sum())
invalid_nav = (nav_history["nav"] <= 0).sum()

#print("\nInvalid NAV values (<=0):")
#print(invalid_nav)


#print(nav_history.dtypes)
#print(nav_history.head())

nav_history.to_csv("data/processed/clean_nav.csv", index=False)

#print("\nclean_nav.csv saved successfully!")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

#print(transactions.head())
#print("\nUnique Transaction Types:")
#print(transactions["transaction_type"].unique())
invalid_amount = (transactions["amount_inr"] <= 0).sum()

#print("\nInvalid Amounts (<=0):")
#print(invalid_amount)
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

#print("\nTransaction Date Type:")
#print(transactions["transaction_date"].dtype)
#print("\nUnique KYC Status:")
#print(transactions["kyc_status"].unique())
transactions.to_csv("data/processed/clean_transactions.csv", index=False)

#print("\nclean_transactions.csv saved successfully!")

#PERFORMANCE 

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

#print(performance.head())       
#print(performance.columns)
#print("\nReturn Column Types:")
#print(performance[["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]].dtypes)
anomalies = performance[
    (performance["return_1yr_pct"] > 100) |
    (performance["return_1yr_pct"] < -100)
]

#print("\nAnomalies in 1-Year Return:")
#print(len(anomalies))
invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

#print("\nInvalid Expense Ratio Rows:")
#print(len(invalid_expense))
performance.to_csv("data/processed/clean_performance.csv", index=False)

#print("\nclean_performance.csv saved successfully!")