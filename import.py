# The program imports data into a database

import csv
import sys
import sqlite3

if len(sys.argv) != 2:
    sys.exit("Usage: import.py filename")

conn = sqlite3.connect("students.db")
db = conn.cursor()

with open(sys.argv[1]) as file:
    reader = csv.reader(file)

    next(reader)
    for line in reader:
        name = line[0].split(" ")
        if len(name) == 2:
            middle_name = "NULL"
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
            (name[0], middle_name, name[1], line[1], line[2]))
            conn.commit()
        else:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
            (name[0], name[1], name[2], line[1], line[2]))
            conn.commit()
