# SQLite first table

import sqlite3

conn = sqlite3.connect("sandeep.db")

curs = conn.cursor()

curs.execute("""CREATE TABLE population (city TEXT, state TEXT, 
             population INT)""")

conn.close()
