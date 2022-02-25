# Initial main file

# SQLITE database functionality to open and manipulate .sqlite files
import sqlite3


con = sqlite3.connect('sqlite-sakila.db')
cur = con.cursor()
cur.execute("SELECT * FROM actor")
rows = cur.fetchall()
for row in rows:
    print(row)
