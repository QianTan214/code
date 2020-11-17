
# method 1: 筛选法

N= 100
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, N + 1):
    for j in range(2 * i, N + 1, i): # 写法很妙
        is_prime[j] = False

res = []
for i in range(len(is_prime)):
    if is_prime[i] == True:
        res.append(i)
print(res)



# method 1 更简单写法
N= 100
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
res = []

for i in range(2, N + 1):
    if is_prime[i]: # 如果是prime number，直接append到res
        res.append(i)
        for j in range(2*i, N+1, i):
            is_prime[j] = False

print(res)





# method 2: 遍历法
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

re = []
for i in range(100):
    if is_prime(i):
        res.append(i)
print(res)




