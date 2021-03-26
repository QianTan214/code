from cs50 import get_int

#no do while loop in python, use while True: instead
while True:

    height = get_int("Height: ")

    if height > 0 and height <= 8:

        break

# be mindful of python print function, it automatically print \n for you
# use end = "" to remove it

for i in range (height):

    for j in range (height - (i+1)):
        print(" ", end = "")

    for k in range (i+1):
        print ("#", end = "")

    print()

