import sqlite3
db = "db.sqlite3"
conn = sqlite3.connect(db)
conn.execute("DROP TABLE schedule" )
conn.commit()
conn.close()
print('success')