
import sqlite3

conn = sqlite3.connect('instance/data.db')
cur = conn.cursor()
result = cur.execute('''SELECT * FROM Entry''')
lst = result.fetchall()
print(lst)
