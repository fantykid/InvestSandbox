import pandas as pd
import sqlite3

db_path = r"C:\Users\fanty\Desktop\InvestSandbox\database\InvestSandbox.db"
file_path ="C:\\Users\\fanty\Desktop\\InvestSandbox\\data\stock_history.xlsx"
file_path2 = "C:\\Users\\fanty\Desktop\\InvestSandbox\\data\\stock_history2.xlsx"

df1 = pd.ExcelFile(file_path)
df2 = pd.ExcelFile(file_path2)

# 假設N/A在資料中為NaN值

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    initial_funds REAL,
    current_funds REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Stocks (
    stock_code TEXT,
    date DATE,
    open_price REAL,
    close_price REAL,
    high_price REAL,
    low_price REAL,
    volume INTEGER,
    PRIMARY KEY (stock_code, date)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    stock_code TEXT,
    transaction_date DATE,
    type TEXT,
    quantity INTEGER,
    transaction_price REAL,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(stock_code) REFERENCES Stocks(stock_code)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Portfolio (
    user_id INTEGER,
    stock_code TEXT,
    quantity INTEGER,
    PRIMARY KEY(user_id, stock_code),
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(stock_code) REFERENCES Stocks(stock_code)
)
''')

for sheet_name in df2.sheet_names:
    # 讀取工具表資料
    df = pd.read_excel(df2, sheet_name=sheet_name)
    df.columns = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
    # 清除N/A的資料
    df.dropna(inplace=True)

    # 假設工具表名稱就是股票代碼
    df['stock_code'] = sheet_name

    df.to_sql('Stocks', conn, if_exists='append', index=False)

conn.commit()
conn.close()