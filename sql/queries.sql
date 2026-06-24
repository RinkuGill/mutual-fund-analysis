-- 1. Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with expense ratio < 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Average transaction amount by type
SELECT transaction_type, AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Top 5 funds by 1-year return
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 7. Count investors by KYC status
SELECT kyc_status, COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 8. Average 3-year return
SELECT AVG(return_3yr_pct) AS avg_3yr_return
FROM fact_performance;

-- 9. Highest Sharpe Ratio funds
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 10. Total investment by transaction type
SELECT transaction_type, SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY transaction_type;