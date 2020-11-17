# BFS可以求从一点出发到其他点的最短距离

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def bfs(graph, start):
    queue = []
    queue.append(start)
    visited = set() # 创建set不能用{}，必须用set()
    visited.add(start)
    parent = {start: None}

    while queue: # while (len(q) > 0)
        vertex = queue.pop(0) # 每次从队列拿一个点出来
        nodes = graph[vertex] # 找到和拿出的点相连的所有点
        for node in nodes:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                parent[node] = vertex
        # print(vertex)
    return parent

parent = bfs(graph, "E")

# 如果从E出发走到B的最短路径
v = "B"
while v != None:
    print(v)
    v = parent[v]

# 结果: E C B

"""
for key in parent:
    print (key, ":", parent[key])


bfs结果:
E : None
C : E # C的前一个点是E
D : E
A : C
B : C
F : D
"""