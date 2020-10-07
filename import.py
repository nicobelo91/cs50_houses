from cs50 import SQL
import csv
import sys

# Check if command line is complete
if len(sys.argv) != 2:
    print("Usage: python houses.py characters.csv")
    sys.exit(1)

# Create database
# open("students.db", "w").close()

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

        first = row["name"]
        house = row["house"]
        birth = row["birth"]

        #writer.writerow([row["name"], row["house"], row["birth"]])
        db.execute("INSERT INTO students(first, house, birth) VALUES(?, ?, ?)",
            first, house, birth)
        #db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)")


