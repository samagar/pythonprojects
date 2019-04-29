# SQLite first table

import sqlite3

conn = sqlite3.connect("sandeep.db")

curs = conn.cursor()

#curs.execute("""CREATE TABLE population1 (city TEXT, state TEXT, 
#              population INT)""")


#curs.execute("INSERT into population1 values('san diego', 'CA', \
#	'1000')")

#conn.commit()

# no need of commit()
#	curs.execute("INSERT into population1 values('los aneglis', 'CA', \
#	'4000')")

cities = [("panvel1","MH",30000),
           ("mumbai1","MH",1000),
           	("abudhabi1","Dub",1000)]
with sqlite3.connect("sandeep.db") as conn:
	curs = conn.cursor()
	curs.executemany('INSERT INTO population1 VALUES(?, ?, ?)', cities)


connect.close()
