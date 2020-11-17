class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    
        """
        lambda 函数的用法，第一个数从大到小排序，第二个数从小到大排序
        insert 函数的用法
        """

        people.sort(key = lambda x: (-x[0], x[1]))
        # sort结果[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        
        res = []
        
        for p in people:
            res.insert(p[1], p)
        return res