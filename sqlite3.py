import sqlite3

conn = sqlite3.connect("InClass.db")


try:

	C = conn.cursor()

	C.execute("Create Table stocks (date text, symbol text, trans text, qty real, price real")

	C.execute("Insert into stocks Values('2015-3-23', 'AAPL', 'BUY', '100' '129.10')")
	C.execute("Insert into stocks Values('2015-3-23', 'GOOG', 'BUY', '200' '127.10')")
	C.execute("Insert into stocks Values('2015-3-23', 'NFLX', 'SELL', '102' '122.10')")

	conn.commit()
except:
	conn.rollback()


conn.close()