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

    while queue: # while (len(q) > 0)
        vertex = queue.pop(0) # 每次从队列拿一个点出来
        nodes = graph[vertex] # 找到和拿出的点相连的所有点
        for node in nodes:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)

bfs(graph, "E")

"""
bfs结果:
E
C
D
A
B
F
"""