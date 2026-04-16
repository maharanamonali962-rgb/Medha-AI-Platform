import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    score INTEGER
)
''')

conn.commit()
conn.close()

print("Database created successfully!")