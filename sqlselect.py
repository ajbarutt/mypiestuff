import sqlite3

conn = sqlite2.connect("Inclass.db")

C = conn.cursor()
Rows = C.execute("Select * from stocks")

for item in Rows:
	print item

conn.close()