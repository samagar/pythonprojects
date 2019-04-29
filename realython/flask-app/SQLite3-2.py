import csv
import sqlite3


with sqlite3.connect("realpython.db") as conn:
	curs = conn.cursor()

	# family = csv.reader(open("names.csv","r"))

	#curs.execute("CREATE TABLE familynames(firstname TEXT, lastname TEXT)")

	
	# curs.executemany("INSERT INTO familynames VALUES(?,?)", family)
	curs.execute("SELECT firstname, lastname from familynames")

	rows = curs.fetchall()

	for r in rows:
		print(r[0], r[1])
		