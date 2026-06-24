# Data Dictionary

## 1. dim_fund

| Column      | Data Type | Description                   |
| ----------- | --------- | ----------------------------- |
| amfi_code   | INTEGER   | Unique AMFI scheme identifier |
| scheme_name | TEXT      | Name of mutual fund scheme    |
| fund_house  | TEXT      | Mutual fund company           |
| category    | TEXT      | Fund category (Equity/Debt)   |
| risk_grade  | TEXT      | Risk level of fund            |

---

## 2. dim_date

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| date_id   | INTEGER   | Unique date identifier |
| full_date | DATE      | Complete date          |
| year      | INTEGER   | Year value             |
| month     | INTEGER   | Month value            |
| day       | INTEGER   | Day value              |

---

## 3. fact_nav

| Column    | Data Type | Description             |
| --------- | --------- | ----------------------- |
| amfi_code | INTEGER   | Fund identifier         |
| date      | DATE      | NAV date                |
| nav       | REAL      | Net Asset Value of fund |

Source: `02_nav_history.csv`

---

## 4. fact_transactions

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | TEXT      | Unique investor ID         |
| transaction_date | DATE      | Transaction date           |
| amfi_code        | INTEGER   | Fund identifier            |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr       | REAL      | Transaction amount in INR  |
| state            | TEXT      | Investor state             |
| city             | TEXT      | Investor city              |
| kyc_status       | TEXT      | KYC verification status    |

Source: `08_investor_transactions.csv`

---

## 5. fact_performance

| Column            | Data Type | Description                       |
| ----------------- | --------- | --------------------------------- |
| amfi_code         | INTEGER   | Fund identifier                   |
| return_1yr_pct    | REAL      | 1-year return percentage          |
| return_3yr_pct    | REAL      | 3-year return percentage          |
| return_5yr_pct    | REAL      | 5-year return percentage          |
| alpha             | REAL      | Excess return over benchmark      |
| beta              | REAL      | Market sensitivity                |
| sharpe_ratio      | REAL      | Risk-adjusted return metric       |
| expense_ratio_pct | REAL      | Annual management fee percentage  |
| aum_crore         | REAL      | Assets under management in crores |

Source: `07_scheme_performance.csv`
