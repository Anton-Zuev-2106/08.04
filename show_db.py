import sqlite3

conn = sqlite3.connect(
    "news.db"
)

cur = conn.cursor()

rows = cur.execute(
    "SELECT * FROM articles LIMIT 20"
)

for row in rows:

    print(row)

conn.close()