import sqlite3

# creates new db if it doesn't exist
conn = sqlite3.connect("new.db")

# retrieve a cursor to execute sql statements

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

conn.close()
