启发式搜索 （有信息搜索）：

1. 贪婪最佳优先搜索greedy best-first search

贪婪最佳优先搜索中 评价函数 = 启发函数
评价函数evaluation function
启发函数heuristic function

贪婪最佳优先搜索并不是最优的


2. A*搜索

评价函数evaluation function
启发函数heuristic function

评价函数f(n) = g(n) + h(n) 起点到当前最小代价 + 当前到目标最小代价

启发函数是可容的(admissible heuristic) 和一致的(consistent)
可容性：如将直线距离作为启发函数，不会高估其开销代价

tree-search
graph-search
