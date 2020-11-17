N = 100
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, N + 1):
    for j in range(2 * i, N + 1, i): # 写法很妙
        is_prime[j] = False

res = [] 
for i, num in enumerate(is_prime):
    if num == True:
        res.append(i)
print (res)

