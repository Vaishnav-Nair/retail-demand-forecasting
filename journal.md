# Retail Demand Forecasting 

## Project Brief
A retail chain is losing revenue through overstocking and stockouts. My job is to build a forecasting system that predict weekly sales per store so the supply chain team can plan inventory better.

---

## Week 1 - Project Setup

### Date: 1st July 2026

### What I did:
- Set up professional folder structure
- Created Github repository
- Installed all required python libraries
- Dowloaded Rossman dataset

### Why I did it:
- Professional folder structure separated raw vs processed data
- Github tracks every change I make throughout the project
- Rossmann is a real retail dataset with 1m+ rows across 1,115 stores

---

## Week 1 - Day2 - Data Exploration

### Date: 9th July 2026

Key Findings so far:

- 1,017,209 rows across 1,115 stores (2013-2015)
- 172,817 rows are closed store days → will filter before modelling
- 54 open stores with zero sales → likely data errors which will be removed
- Sales is right-skewed → will use log transformation during modelling
- Store data has missing values in competition and promo2 columns → missing promo2 means store doesn’t participate, not bad data

Decisions made:

- Filter out open=0 rows before training
- Use np.log1p() to transform Sales target variable
- Will need to handle mixed types in StateHoliday column

---

## Week 1 - Day3 - Key Bussiness Insights Found

### Date: 10th July 2026

### Sales Patterns:
- December sales are ~30% higher than average months (Christmas effect)
- Monday and Sunday are highest sales days (~€8,000 avg)
- Saturday is the lowest sales day (~€5,900 avg)

### Promo Impact:
- Promotions drive a 38.8% sales lift (€5,929 -> €8,228)
- This makes 'Promo' one of the most important features for our forecasting model

### Data Quality:
- 172,817 closed store days -> will filter before modelling
- 54 open stores with zero sales -> will remove as data errors
- Sales is right skewed -> will apply log transformation

### Feature Engineering Decisions (based on EDA):
- DayOfWeek will be a strong feature
- Month/seasonal features are essential (December effect)
- Promo is critical - 38.8% lift confirmed

---

## Week 2 — Day 1: Store Type Analysis
### Date: 24th September 2026

### What I did:
- Completed Cell 10 - Store Type Analysis
- Merged open_df with store_df
- Grouped by StoreType and visualised average sales

### What I learned:
- .merge() with how='left' keeps all rows from left dataframe
- groupby() splits → applies function → returns one result per group
- result.index and result.values for plotting grouped data
- Always match x and y size before plotting (learned from my mistake)

### Key Finding:
- Store Type B averages €10,231 — 48% higher than other types
- StoreType will be an important feature in our model

### Mistake I made and fixed:
- Used store_df['StoreType'] instead of result.index
- x had 1,115 rows, y had 4 — size mismatch error

## Week 2 Day 2 — SQL Database Setup & Queries
### Date: 14th October 2026

### What I did:
- Created SQLite database (rossmann.db) using sqlite3 and pandas
- Loaded sales table (1,017,209 rows) and stores table (1,115 rows)
- Wrote 5 business SQL queries using queries.py

### Queries I wrote:
1. SELECT * FROM sales LIMIT 5 → first look at database
2. Average sales by store type using JOIN
3. Top 10 stores by total revenue using SUM + ORDER BY + LIMIT
4. Promo impact using AVG + WHERE + GROUP BY
5. Monthly revenue using strftime() + GROUP BY

### What I learned:
- sqlite3.connect() creates a real database file
- pd.read_sql() runs SQL queries and returns a pandas dataframe
- JOIN combines two tables using a shared column (Store)
- WHERE filters rows before grouping (like boolean indexing in pandas)
- GROUP BY collapses many rows into one row per group
- strftime('%m', Date) extracts month number from a date
- SUM vs AVG tell different stories — always question which one fits
- GROUP BY in SQL = .groupby() in pandas — same concept different syntax

### Key Business Findings:
- Store Type B averages €10,058 — 48% higher than other store types
- Store 262 is top performer → €19,516,842 total revenue
- Promotions drive 38.8% sales lift (€5,929 → €8,228) — confirmed in SQL
- March has highest TOTAL revenue but December has highest AVERAGE per store
- Total vs average tell different stories — always clarify which metric fits

### Mistakes I made and fixed:
- JOIN ON wrong columns (Store = StoreType) → fixed to sales.Store = stores.Store
- Selected wrong column in promo query → learned to always SELECT what you need
- Forgot WHERE Open = 1 → closed store days dragged promo average down
- Had extra Date column in SELECT → caused grouping by year instead of month
- GROUP BY month failed → learned to use AS to name columns first

### SQL vs Pandas equivalents I now know:
- pd.read_csv() → SELECT * FROM table
- df.merge() → JOIN
- df[df['Open']==1] → WHERE Open = 1
- df.groupby() → GROUP BY
- df.sort_values() → ORDER BY
- df.head(10) → LIMIT 10



