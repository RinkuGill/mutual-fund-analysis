import requests
import pandas as pd

# Fund names and their AMFI codes
funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

# Loop through each fund
for fund_name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching data for {fund_name}...")

    response = requests.get(url)
    data = response.json()

    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    file_path = f"data/raw/{fund_name}_nav.csv"
    df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")

print("\nAll 5 fund NAV files saved successfully!")