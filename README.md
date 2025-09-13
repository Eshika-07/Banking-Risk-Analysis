![Banking Risk Analysis](https://github.com/Eshika-07/Banking-Risk-Analysis/blob/main/Banking%20Dashboard.png)

# Banking Risk Analysis

## Problem Statement
Develop a basic understanding of **risk analytics** in banking and financial services, and explore how **data** can be used to minimise the risk of losing money while lending to customers.

---

## Solution Approach

1. **Data Ingestion**
   - Raw data in **CSV** format.
   - A Python script is used to **dump CSV data into a SQL database** for structured storage and querying.
2. **Exploratory Data Analytics**
   - Data is loaded from the SQL database into a pandas DataFrame
   - Performed data cleaning, feature understanding, and statistical summaries
   - Generated multiple visualisations to identify trends, correlations, and risk factors
3. **Visual Analysis**
   - Used Matplotlib and Seaborn for plotting


---

## Business Insights
- Older customers tend to maintain higher account balances. This may indicate greater financial stability, which can reduce lending risk
- Customers in certain geographies (e.g., Germany) show higher activity rates, potentially reflecting stronger engagement with banking products
- Higher balances and longer tenure could be used as low-risk indicators when approving loans
- Dormant high-balance accounts present an opportunity for cross-selling or reactivation campaigns
- Targeted engagement in lower-credit-score geographies could improve repayment behaviour



---

## Tech Stack
- Python (pandas, matplotlib, seaborn, sqlite3)
- SQL Database (MYSQL)
- Jupyter Notebook for EDA

---

## Future Improvements
- Implement machine learning models for risk prediction
- Automate data pipeline from ingestion to reporting
- Integrate dashboard for real-time risk monitoring
