from cs50 import SQL
import csv
import sys

# Check if command line is complete
if len(sys.argv) != 2:
    print("Usage: python roster.py choose-house")
    sys.exit(1)
    
chosenHouse = sys.argv[1]

# Open students.db for SQLite
db = SQL("sqlite:///students.db")

rows = db.execute("SELECT first, middle, last, birth FROM students WHERE house = (?) ORDER BY last, first", chosenHouse)
count = len(rows)
i = 0
while i <= count:
    firstName = rows[i]["first"]
    lastName = rows[i]["last"]
    birthDate = rows[i]["birth"]
    if (rows[i]["middle"] != None):
        middleName = rows[i]["middle"]
        print(firstName, middleName, lastName, end=",")
        print(birthDate)
    else:
        print(firstName, lastName, end=",")
        print(birthDate)
    i += 1