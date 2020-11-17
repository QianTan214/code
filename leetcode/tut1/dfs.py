graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}
# print(graph.keys)

def dfs(graph, start):
    stack = []
    stack.append(start)
    visited = set() # 创建set不能用{}，必须用set()
    visited.add(start)

    while stack: # while (len(q) > 0)
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in visited:
                stack.append(node)
                visited.add(node)
        print(vertex)

dfs(graph, "E")

"""
bfs结果:
E
D
F
B
A
C
"""