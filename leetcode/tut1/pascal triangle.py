# range(0, 0) -- 不对

# 二维数组N * N全是0, [[0]*N]

N = 10
tri = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    tri.append(row)
# print(tri)
# 用numpy打印出来更好看

# tri = [[0]*N]*N 
# 这种方法创建出来的二维数组其实是五个备份，改其中一个，其他的也改了，所以最好不用这种方法

for i in range(N):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = 1
        elif i == j:
            tri[i][j] = 1
        else:
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
# print(tri) 

# 判断杨辉三角里最大的数是几位数
# print(max(tri)) # 结果: [1, 5, 10, 10, 5, 1]
# print(max(max(tri))) # 结果: 10

max_value = max((max(tri)))

digits = len(str(max_value))

# num表示数字，n表示想以几位数形式打印出来，位数不足用空格补在数字前面
def print_number(num, n):
    space = n - len(str(num))
    print(space * " " + str(num), end = "")

def print_space(n):
    for i in range(n):
        print(" ", end = "")

# 遍历杨辉三角
for i in range(N):
    space = N - i - 1
    for k in range(space):
        print_space(digits)
    for j in range(i+1):
        print_number(tri[i][j], digits)
        print_space(digits)
    print()

