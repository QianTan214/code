
# 华氏温度转成摄氏温度

f = float(input("请输入华氏温度: ")) # Fahrenheit/Celsius
c = (f - 32) / 1.8
print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")

# 判断是不是闰年

year = int(input("请输入年份： "))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)

# 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')


# 用for循环实现1~100之间的偶数求和
total = 0
for i in range(2,101,2):
    total += i
print(total)



# 猜数字游戏
import random

answer = random.randint(1, 100) # 产生一个1-100范围的随机数
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break

print(f'你总共猜了{counter}次')


# 九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i * j}", end = "\t")
    print()



# 输入一个正整数判断它是不是素数

num = int(input('请输入一个正整数: '))
end = int(num ** 0.5) # 求根号
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')




# 输入两个正整数计算最大公约数和最小公倍数

x = int(input("x: "))
y = int(input("y: "))

if x > y:
    x, y = y, x

for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'{x}和{y}的最大公约数是{i}')
        print(f'{x}和{y}的最小公倍数是{x * y // i}')
        break



# 向列表容器中逆向插入10个元素

nums = []
for i in range(10):
    nums.insert(0, i) # If index is 0, the element is inserted at the beginning of the list.
print(nums)

# 向列表容器中逆向插入10个元素

nums = []
for i in range(100000):
    nums.append(i)
nums.reverse()


# 生成Fibonacci数列（前100个Fibonacci数）

# lambda

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

# 递推

a, b = 0, 1
for num in range(1, 101):
    a, b = b, a + b
    print(f'{num}: {a}')

# 改进的递归

from functools import lru_cache

@lru_cache() # 装饰器
def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)

for num in range(1, 101):
    print(f'{num}: {fib(num)}')

"""
Python中使用@lru_cache装饰器能加快函数运行，
其中LRU指least recent used —— 最近使用过的计算结果会保留在这个容量有限的池子中。
为了避免池中内容无限制地增加，会清除不常用的计算结果。

由于对简单的斐波那契数列算法应用了@lru_cache装饰器，每次调用fibc(n)时，
都会检查由装饰器维护的缓存池。如果参数n在缓存池中，
直接使用对应的计算结果，避免了重复计算导致的成本增加。每次计算的结果都会保存到缓存池中。
"""


# 百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，
# 用100元买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

for i in range(21):
    for j in range(34):
        k = 100 - i - j
        if k % 3 == 0 and 5 * i + 3 * j + k // 3 == 100:
            print(i, j , k)



# 五人分鱼问题：ABCDE五人在某天夜里合伙捕鱼，最后疲惫不堪各自睡觉。
# 第二天A第一个醒来，他将鱼分为5份，扔掉多余的1条，拿走了属于自己的一份；
# B第二个醒来，也将鱼分为5份，扔掉多余的1条，拿走属于自己的一份；
# 然后C、D、E依次醒来，也按同样的方式分鱼，问他们至少捕了多少条鱼？

fish = 1
while True:
    total, enough = fish, True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1)  //  5 * 4
        else:
            enough = False
            break
    if enough:
        print(f'总共有{fish}条鱼')
        break
    fish += 1



# 爬楼梯 - 楼梯有n个台阶，一步可以走1阶、2阶或3阶，走完n个台阶共有多少种不同的走法。

from functools import lru_cache

@lru_cache()
def climb(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n >= 3:
        return climb(n-1)+ climb(n-2) + climb(n-3)

for i in range(1, 10):
    print(climb(i))


# 变态台阶问题: 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""

分析：用Fib(n)表示跳上n阶台阶的跳法数。如果按照定义，Fib(0)肯定需要为0，否则没有意义。
但是我们设定Fib(0) = 1；n = 0是特殊情况，通过下面的分析就会知道，强制令Fib(0) = 1很有好处。
ps. Fib(0)等于几都不影响我们解题，但是会影响我们下面的分析理解。

当n = 1 时， 只有一种跳法，即1阶跳：Fib(1) = 1;

当n = 2 时， 有两种跳的方式，一阶跳和二阶跳：Fib(2)  = 2;

到这里为止，和普通跳台阶是一样的。

当n = 3 时，有三种跳的方式，第一次跳出一阶后，对应Fib(3-1)种跳法； 
第一次跳出二阶后，对应Fib(3-2)种跳法；第一次跳出三阶后，只有这一种跳法。
Fib(3) = Fib(2) + Fib(1)+ 1 = Fib(2) + Fib(1) + Fib(0) = 4;

当n = 4时，有四种方式：第一次跳出一阶，对应Fib(4-1)种跳法；
第一次跳出二阶，对应Fib(4-2)种跳法；第一次跳出三阶，对应Fib(4-3)种跳法；
第一次跳出四阶，只有这一种跳法。
所以，Fib(4) = Fib(4-1) + Fib(4-2) + Fib(4-3) + 1 = Fib(4-1) + Fib(4-2) + Fib(4-3) + Fib(4-4) 种跳法。

当n = n 时，共有n种跳的方式，第一次跳出一阶后，后面还有Fib(n-1)中跳法； 
第一次跳出二阶后，后面还有Fib(n-2)中跳法...
第一次跳出n阶后，后面还有 Fib(n-n)中跳法。Fib(n) = Fib(n-1)+Fib(n-2)+Fib(n-3)+...+Fib(n-n) = Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)。

通过上述分析，我们就得到了通项公式：
Fib(n) =  Fib(0)+Fib(1)+Fib(2)+.......+ Fib(n-2) + Fib(n-1)
因此，有 Fib(n-1)=Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-2)

两式相减得：Fib(n)-Fib(n-1) = Fib(n-1)  =====》 Fib(n) = 2*Fib(n-1)   n >= 3

这就是我们需要的递推公式：Fib(n) = 2*Fib(n-1)  n >= 3


"""

fib = lambda n: n if n <= 2 else 2 * fib(n - 1)



# 矩形覆盖
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法?


"""
我们先把2x8的覆盖方法记为f(8)。
用第一个1x2小矩阵覆盖大矩形的最左边时有两个选择，竖着放或者横着放。
当竖着放的时候，右边还剩下2x7的区域，这种情况下的覆盖方法记为f(7)。
接下来考虑横着放的情况。当1x2的小矩形横着放在左上角的时候，左下角横着放一个1x2的小矩形，
而在右边还剩下2x6的区域，这种情况下的覆盖方法记为f(6)。
因此f(8)=f(7)+f(6)。此时我们可以看出，这仍然是斐波那契数列。


先从简单的开始分析，1个2*1竖着放的话会占掉大矩形1列的空间，
2个小矩形横着放的话会占掉大矩形2列的空间，
所以本题可以改成大矩形所有列都被小矩形占据的话有多少种方法
"""

fib = lambda n : n if n <= 2 else fib(n - 1) + fib (n - 2)

for i in range(10):
    a = fib(i)
    print(a, end = " ")
print()