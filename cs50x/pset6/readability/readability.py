from cs50 import get_string


st = get_string ("Text: ")

letter = 0

for i in range (0, len(st)):
    if (st[i] >='a' and st[i] <='z') or (st[i] >='A' and st[i] <='Z'):
        letter = letter + 1

word = 1

for i in range (0, len(st)):
    if (st[i] ==' '):
        word = word + 1


sentence = 0

for i in range (0, len(st)):
    if (st[i] =='.' or st[i] =='!' or st[i] == '?' ):
        sentence = sentence + 1



L = 100 * letter / word

S = 100 * sentence / word


grade = 0.0588 * L - 0.296 * S - 15.8

grade = round(grade)


if grade >= 16:
    print (f"Grade 16+")
elif grade < 1:
    print (f"Before Grade 1")
else:
    print(f"Grade {grade}")