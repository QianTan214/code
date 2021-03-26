"""
For each student in the CSV file, insert the student into the students table in the students.db database.
While the CSV file provided to you has just a name column, the database has separate columns for first, middle,
and last names. You’ll thus want to first parse each name and separate it into first, middle, and last names.
You may assume that each person’s name field will contain either two space-separated names (a first and last name) or
#three space-separated names (a first, middle, and last name).
#For students without a middle name, you should leave their middle name field as NULL in the table.

"""


from sys import argv, exit
import csv
import cs50

def main():

    if len(argv) !=2:
        print("missing command-line arguments")
        exit (1)

    # import SQL from cs50, connect database in python
    db=cs50.SQL("sqlite:///students.db")


    #open CSV file
    with open (argv[1], "r") as file:
        reader = csv.DictReader(file, delimiter= ",")
        for row in reader:
            if row["name"]:
                fullname = row["name"].split(" ") # fullname is a list
                firstname = fullname[0]
                if len(fullname) == 3:
                    middlename = fullname[1]
                    lastname = fullname[2]
                else:
                    middlename = None
                    lastname = fullname[1]
                birthday = int(row["birth"])
                db.execute("insert into students (first, middle, last, house, birth) values (?, ?, ?, ?, ?)", firstname, middlename, lastname, row["house"], birthday)


#use below syntax to check out students database in command window
#sqlite3 students.db and .schema
#select * from students limit 10;


main()
