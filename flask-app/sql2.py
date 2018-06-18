# new table in sandeep.db

import sqlite3

conn = sqlite3.connect("sandeep.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE cars(make TEXT, Model TEXT, quantity INT)""")

conn.close()