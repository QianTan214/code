"""
Given an m x n 2d grid map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            grid[i][j] = '0'
            q = [(i, j)] # 栈
            while q:
                x, y = q.pop()
                if x > 0 and grid[x-1][y] == '1': # (i, j)坐标的上面一点是'1'，则把它变成'0'
                    grid[x-1][y] ='0'
                    q.append((x -1, y))
                if y > 0 and grid[x][y-1] == '1':
                    grid[x][y-1] ='0'
                    q.append((x, y-1))
                if x < m-1 and grid[x+1][y] == '1':
                    grid[x+1][y] ='0'
                    q.append((x+1, y))
                if y < n-1 and grid[x][y+1] == '1':
                    grid[x][y+1] ='0'
                    q.append((x, y+1))
        
        m = len(grid)
        if m == 0:
            return 0
        
        n = len(grid[0])
        res = 0
        
        for i in range(m): # 遍历二维矩阵
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res