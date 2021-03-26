from sys import argv, exit
from cs50 import get_string
import csv


def main():

    if len(argv) != 3:
        print ("missing command-line argument")
        exit (1)

    # open csv file
    database = open(argv[1])
    data = csv.DictReader(database)


    # oepn text file
    with open(argv[2]) as textfile:
        text = textfile.read()

    # get the counts for each STR from DNA sequence
    counts = {}

    for subseq in data.fieldnames[1:]:
        counts[subseq] = most_appear (text, subseq)

    for row in data:
        if all(counts[subseq] == int(row[subseq]) for subseq in counts): # csv file stores strings, need to convert to int
            print(row["name"])
            return


    print("No match")




# define a function that calculates STR counts in DNA sequence

def most_appear (str, sub):

    most = 0


    # loop through each character each time, once find the matching substring,
    # loop through "len(sub)" characters each time. (eg. 5 for "AGATC")

    for i in range(len(str)):

        count = 0

        while True:
            start = i + count * len(sub)
            end = start + len(sub)
            if str[start : end] == sub:
                count = count + 1
            else:
                break

        most = max(count, most)

    return most


main()