# N * N二维数组创建
# yield的用法


grid = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    grid.append(row)

# print(grid)

import numpy as np

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False

    for i in range(0,9):
        if grid[i][x] == n:
            return False

    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        yield from solve()
                        grid[y][x] = 0 
                return 
    yield np.matrix(grid) # 用np.matrix 打印没有逗号

s = solve() # s is a generator object

print(next(s))
