import sqlite3
import pandas as pd

conn = sqlite3.connect('data/rossmann.db')

data_sql_1 = pd.read_sql("""SELECT * FROM sales LIMIT 5""", con=conn)
print(data_sql_1)

data_sql_2 = pd.read_sql("""
SELECT stores.StoreType, AVG(sales.Sales)
FROM sales
JOIN stores ON sales.Store = stores.Store
GROUP BY storetype
""", con=conn)
print(data_sql_2)

data_sql_3 = pd.read_sql("""
SELECT Store, SUM(sales.Sales)
FROM sales
GROUP BY store
ORDER BY SUM(Sales) DESC
LIMIT 10
""", con=conn)
print(data_sql_3)

data_sql_4 = pd.read_sql("""
SELECT Promo, AVG(Sales)
FROM sales
WHERE Open = 1
GROUP BY Promo
ORDER BY SUM(Sales) DESC
LIMIT 10
""", con=conn)
print(data_sql_4)

data_sql_5 = pd.read_sql("""
SELECT SUM(Sales), strftime('%m', Date) AS month
FROM sales
GROUP BY month
ORDER BY SUM(Sales) DESC
""", con=conn)
print(data_sql_5)

conn.close()