import sqlite3
db = "db.sqlite3"
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT * From shift Where shift.user_id ==1" )
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()
print('success')