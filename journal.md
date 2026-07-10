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

## Week 2 - Day2 - Data Exploration

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

## Week 2 - Day3 - Key Bussiness Insights Found

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

