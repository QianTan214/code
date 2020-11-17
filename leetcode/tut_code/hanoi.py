def move(f, t):
    print(f"Move disc from {f} to {t} !")

# n discs, from a via b to c
def move_via(n, a, b, c):
    if n == 0:
        pass  
    else:
        move_via(n-1, a, c, b) # n = 1时，n-1 = 0，会pass
        move(a, c)
        move_via(n-1, b, a, c)

disc_num = input("How many discs in total： ")
disc_num = int(disc_num)

move_via(disc_num, "a", "b", "c")