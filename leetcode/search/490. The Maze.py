# premium question
# no access

m, n = len(maze), len(maze[0])

directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

visited = set()

stack = [start]
while stack: # 栈非空时做dfs
    curx, cury = stack.pop()
    if [curx, cury] == destination:
        return True
    for dirx, diry in directions:
        tx, ty = curx, cury
        while 0 <= tx + dirx < m and 0 <= ty + diry < n and not maze[tx + dirx][ty + diry]:
            tx, ty = tx + dirx, ty + diry
        if (tx, ty) not in visited:
            visited.add((tx, ty))
            stack.append((tx, ty))
return False
