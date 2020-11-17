import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

# print(np.matrix(grid)) # np.matrix打印没有逗号

def possible(y,x,n):
    # search in rows
    for i in range(9):
        if grid[y][i] == n:
            return False
    # search in cols
    for i in range(9):
        if grid[i][x] == n:
            return False

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    # search in 3*3 cells
    for i in range(3):
        for j in range(3):
            if grid[y1+i][x1+j] == n:
                return False
    return True

print(possible(4,4,5)) # 结果 True


def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if possible(i,j,k):
                        grid[i][j] = k
                        solve()
                        grid[i][j] = 0 # backtracking
                return 
    print(np.matrix(grid))

solve()