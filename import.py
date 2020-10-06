from cs50 import SQL
import csv
import sys

# Check if command line is complete
if len(sys.argv) != 2:
    print("Usage: python houses.py characters.csv")
    sys.exit(1)
    
# Create database
open("students.db", "w").close()
db = SQL("sqlite:///students.db")

# Create tables
db.execute("INSERT")
    
# Open csv file and read into memory
with open(f"{sys.argv[1]}", 'r') as characters:

    # Create DictReader
    reader = csv.DictReader(characters, delimiter=",")
    
    # Iterate over CSV file
    for row in reader:
        
        