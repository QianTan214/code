# prime number 遍历法

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

res = []

n = input("input a number: ")
n = int(n)

for i in range(n + 1):
    if is_prime(i):
        res.append(i)
print(res)





    


