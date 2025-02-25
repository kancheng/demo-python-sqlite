# demo-python-sqlite

## Note.

以下是使用 Python 中的 `sqlite3` 庫來實作簡單的 SQLite 操作的範例：

### 1. 建立資料庫並連接
```python
import sqlite3

# 連接到 SQLite 資料庫（如果資料庫不存在，則會自動創建）
conn = sqlite3.connect('example.db')

# 創建一個 cursor 物件，用來執行 SQL 語句
cursor = conn.cursor()
```

### 2. 建立資料表
```python
# 創建一個名為 "users" 的資料表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

# 提交變更並關閉連接
conn.commit()
```

### 3. 插入資料
```python
# 插入一筆資料
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# 插入多筆資料
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 40)
])

# 提交變更
conn.commit()
```

### 4. 查詢資料
```python
# 查詢所有資料
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 顯示查詢結果
for row in rows:
    print(row)
```

### 5. 更新資料
```python
# 更新資料
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (32, "Alice"))
conn.commit()
```

### 6. 刪除資料
```python
# 刪除資料
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()
```

### 7. 關閉連接
```python
# 關閉連接
conn.close()
```

這個範例展示了如何使用 `sqlite3` 建立資料庫、資料表，進行資料插入、查詢、更新、刪除等基本操作。
