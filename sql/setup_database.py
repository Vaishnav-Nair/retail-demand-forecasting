import sqlite3
import pandas as pd

conn = sqlite3.connect('data/rossmann.db')

train_df = pd.read_csv('data/raw/train.csv', parse_dates=['Date'])
store_df = pd.read_csv('data/raw/store.csv')

train_df.to_sql(name='sales', con=conn, if_exists='replace', index=False)
print('sales loaded successfully')

store_df.to_sql(name='stores', con=conn, if_exists='replace', index=False)
print('stores loaded successfully')

conn.close()