"""In roster.py, write a program that prints a list of students for a given house in alphabetical order.

Your program should accept the name of a house as a command-line argument.
If the incorrect number of command-line arguments are provided, your program should print an error and exit.
Your program should query the students table in the students.db database for all of the students in the specified house.
Your program should then print out each student’s full name
and birth year (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
Each student should be printed on their own line.
Students should be ordered by last name. For students with the same last name, they should be ordered by first name.

"""

import cs50
from sys import argv, exit
import csv

def main():

    if len(argv) != 2:
        print("missing comman-line argument")
        exit (1)



    # import SQL from cs50, connect database in python
    db = db=cs50.SQL("sqlite:///students.db")

    # argv[0] is roster.py script
    housename = str(argv[1])

    # select systax returns a list of dictionaries
    # note the use of "?" in select syntax
    result = list()
    result = db.execute("select * from students where house = ? order by last, first", housename)


    for row in result:
        firstname = row["first"]
        middlename = row["middle"]
        lastname = row["last"]
        year = row["birth"]

        # should be None here, not 'NULL'
        if middlename == None:
            print(f"{firstname} {lastname}, born {year}")
        else:
            print(f"{firstname} {middlename} {lastname}, born {year}")


#use below syntax to check out students database in command window
#sqlite3 students.db and .schema
#select * from students limit 10;


main()