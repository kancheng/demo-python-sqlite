import sqlite3

print('連接到 SQLite 資料庫')

# 連接到 SQLite 資料庫（如果資料庫不存在，則會自動創建）
conn = sqlite3.connect('example.db')


print('創建一個 cursor 物件，用來執行 SQL 語句')
# 創建一個 cursor 物件，用來執行 SQL 語句
cursor = conn.cursor()


print('創建一個名為 "users" 的資料表')
# 創建一個名為 "users" 的資料表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

print('提交變更並關閉連接')
# 提交變更並關閉連接
conn.commit()

print('插入一筆資料')
# 插入一筆資料
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

print('插入多筆資料')
# 插入多筆資料
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 40)
])

print('提交變更')
# 提交變更
conn.commit()

print('查詢所有資料')
# 查詢所有資料
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print('顯示查詢結果')
# 顯示查詢結果
for row in rows:
    print(row)

print('關閉連接')
# 關閉連接
conn.close()