from cs50 import SQL
import csv
import sys

# Check if command line is complete
if len(sys.argv) != 2:
    print("Usage: python houses.py characters.csv")
    sys.exit(1)

# Create database
# psetopen("students.db", "w").close()

# Open students.db for SQLite
db = SQL("sqlite:///students.db")

# Create table
# db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

# Open csv file and read into memory
with open(f"{sys.argv[1]}", 'r') as characters:

    # Create DictReader
    reader = csv.DictReader(characters)

    # Iterate over CSV file
    for row in reader:

        #for name in row["name"].split():
        fullName = row["name"].split()

        #first = row["name"][0]
        #middle = row["name"][1]
        #last = row["name"][2]
        first = fullName[0]
        house = row["house"]
        birth = row["birth"]

        count = len(fullName)
        if count == 2:
            middle = ""
            last = fullName[1]
        else:
            middle = fullName[1]
            last = fullName[2]

        #writer.writerow([row["name"], row["house"], row["birth"]])
        #db.execute("INSERT INTO students(first, house, birth) VALUES(?, ?, ?)",
        #    first, house, birth)
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
        first, middle, last, house, birth)
