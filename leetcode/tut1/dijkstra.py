# 优先队列 priority queue

import heapq
import math

graph = {
    "A": {"B": 5, "C": 1}, # AB间距离5，AC间距离1
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

def init_distance(graph, start):
    distance = {start: 0}
    for v in graph:
        if v != start:
            distance[v] = math.inf
    return distance


def dijkstra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    visited = set() # 创建set不能用{}，必须用set()
    visited.add(start)
    parent = {start: None}
    distance = init_distance(graph, start)

    while pqueue: # while (len(q) > 0)
        pair = heapq.heappop(pqueue) # 每次从队列拿一个点出来
        dist = pair[0]
        vertex = pair[1]
        visited.add(vertex)

        nodes = graph[vertex].keys() # 找到和拿出的点相连的所有点
        for node in nodes:
            if node not in visited:
                if dist + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph[vertex][node]

    return parent, distance

parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)


"""
运行结果：
{'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'D'}
{'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}

"""