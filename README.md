# 📊 Mutual Fund Analytics Platform

An end-to-end **Data Analytics** project built using **Python, SQL, SQLite, Pandas, NumPy, and Financial Analytics** to analyze mutual fund performance, investor behavior, and risk metrics.

This project simulates a real-world fintech analytics pipeline by collecting mutual fund data, cleaning and transforming it, storing it in a relational database, performing exploratory and financial analysis, and generating meaningful insights for investment decision-making.

---

# 🚀 Project Overview

The Indian Mutual Fund industry manages trillions of rupees across thousands of investment schemes. Investors often struggle to compare mutual funds because important information such as NAV history, AUM, SIP inflows, benchmark indices, and portfolio holdings are available from multiple sources.

This project integrates all these datasets into a single analytics platform that enables:

- Mutual fund performance analysis
- Risk-adjusted return analysis
- Investor behavior analysis
- Benchmark comparison
- Advanced financial metrics
- Data-driven investment insights

---

# 🎯 Project Objectives

- Build an ETL pipeline for mutual fund datasets
- Clean and preprocess financial datasets
- Store cleaned data in SQLite
- Perform SQL-based analysis
- Conduct Exploratory Data Analysis (EDA)
- Compute financial performance metrics
- Build advanced risk analytics
- Generate reports for investment insights

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib |
| Statistics | SciPy |
| Database | SQLite |
| ORM | SQLAlchemy |
| Notebook | Jupyter Notebook |
| Version Control | Git & GitHub |
| IDE | VS Code |
| API | mfapi.in |

---

# 📂 Project Structure

```
mutual-fund-analysis/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── sql/
│
├── dashboard/
│
├── data_ingestion.py
├── cleaning.py
├── database_load.py
├── live_nav_fetch.py
├── Performance_Analytics.ipynb
├── Advanced_Analytics.ipynb
├── bluestock_mf.db
├── requirements.txt
└── README.md
```

---

# 📁 Datasets Used

The project uses ten datasets.

| Dataset | Description |
|----------|-------------|
| Fund Master | Master information of all mutual fund schemes |
| NAV History | Daily NAV values of all funds |
| AUM by Fund House | Quarterly Assets Under Management |
| Monthly SIP Inflows | SIP inflow statistics |
| Category Inflows | Net inflows by mutual fund category |
| Industry Folio Count | Total investor folios |
| Scheme Performance | Fund returns and expense ratio |
| Investor Transactions | SIP, Redemption & Lumpsum transactions |
| Portfolio Holdings | Stocks held by each mutual fund |
| Benchmark Indices | Nifty 50, Nifty 100 and other benchmark data |

---

# ⚙️ Project Workflow

```
Raw CSV Files
        │
        ▼
Data Ingestion
        │
        ▼
Data Cleaning
        │
        ▼
Processed Data
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Performance Analytics
        │
        ▼
Advanced Risk Analytics
        │
        ▼
Final Reports
```

---

# 📥 Phase 1 — Data Ingestion

### Tasks Performed

- Loaded all datasets using Pandas
- Checked shape, data types and missing values
- Validated AMFI codes
- Verified duplicate records
- Built project folder structure
- Generated requirements.txt

### Live API Integration

Integrated the **mfapi.in** API to fetch live NAV data for multiple mutual fund schemes.

Funds fetched:

- SBI Bluechip
- HDFC Top 100
- ICICI Bluechip
- Nippon Large Cap
- Kotak Bluechip

---

# 🧹 Phase 2 — Data Cleaning

Performed comprehensive preprocessing on all datasets.

Tasks included:

- Missing value handling
- Duplicate removal
- Data type conversion
- Date formatting
- Transaction validation
- NAV validation
- Standardization of categorical values

Generated clean datasets for further analysis.

---

# 🗄️ Phase 3 — Database Design

Designed and implemented a SQLite database.

Created structured tables for:

- Fund Master
- NAV History
- Transactions
- Performance
- AUM

Loaded cleaned datasets using SQLAlchemy.

---

# 📝 SQL Analysis

Performed analytical SQL queries including:

- Top funds by AUM
- Monthly NAV analysis
- Transaction analysis
- Fund category analysis
- Expense ratio comparison
- Investor insights

---

# 📈 Exploratory Data Analysis (EDA)

Performed comprehensive EDA on all datasets.

Analysis included:

- AUM Growth
- Monthly SIP Trends
- Category Inflows
- Investor Demographics
- Transaction Distribution
- Industry Folio Growth
- Portfolio Analysis
- Benchmark Trends

Generated multiple charts and business insights.

---

# 📊 Performance Analytics

Calculated various financial metrics for all mutual funds.

## Daily Returns

Calculated daily percentage change in NAV.

---

## CAGR

Calculated

- 1-Year CAGR
- 3-Year CAGR
- 5-Year CAGR

---

## Sharpe Ratio

Measured risk-adjusted return.

---

## Sortino Ratio

Measured downside risk-adjusted return.

---

## Alpha

Calculated excess return over benchmark.

---

## Beta

Measured fund volatility relative to market.

---

## Maximum Drawdown

Calculated maximum historical decline.

---

## Fund Scorecard

Developed a composite ranking model based on:

- 3-Year Return
- Sharpe Ratio
- Alpha
- Expense Ratio
- Maximum Drawdown

---

## Tracking Error

Measured deviation from benchmark index.

---

# 📊 Reports Generated

- fund_scorecard.csv
- alpha_beta.csv
- benchmark_comparison.png

---

# 📈 Advanced Analytics (In Progress)

The project is being extended with advanced financial analytics including:

- Historical Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation System
- Sector Concentration Analysis (HHI)

Expected Deliverables:

- Advanced_Analytics.ipynb
- var_cvar_report.csv
- recommender.py
- rolling_sharpe_chart.png

---

# 💻 Skills Demonstrated

- Python Programming
- Data Cleaning
- ETL Pipeline
- Financial Analytics
- SQL
- SQLite
- API Integration
- Statistical Analysis
- Risk Analytics
- Data Visualization
- Version Control using Git & GitHub

---

# 📌 Key Financial Metrics Used

- Daily Return
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

---

# 📚 Learning Outcomes

This project helped develop practical experience in:

- End-to-End Data Analytics
- Financial Data Analysis
- Mutual Fund Analytics
- Risk Measurement
- SQL Database Design
- Python Automation
- API Integration
- Business Intelligence
- Data Storytelling

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/RinkuGill/mutual-fund-analysis.git
```

### Navigate to Project

```bash
cd mutual-fund-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Ingestion

```bash
python data_ingestion.py
```

### Run Data Cleaning

```bash
python cleaning.py
```

### Load Database

```bash
python database_load.py
```

### Fetch Live NAV

```bash
python live_nav_fetch.py
```

Open Jupyter Notebook for analytics:

- Performance_Analytics.ipynb
- Advanced_Analytics.ipynb

---

# 📌 Future Enhancements

- Complete advanced risk analytics
- Improve recommendation engine
- Automate ETL pipeline
- Deploy analytics as a web application
- Add scheduled live NAV updates
- Build portfolio optimization module

---

# 👨‍💻 Author

**Rinku Gill**

Computer Science Engineer | Data Analyst

Skills:

- Python
- SQL
- Data Analytics
- Machine Learning
- Financial Analytics
- Power BI

GitHub:
https://github.com/RinkuGill

LinkedIn:
https://www.linkedin.com/in/rinku-gill-37997432b/

---

## ⭐ If you found this project useful, consider giving it a star!