class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # 用最少的箭射气球问题
        # 贪心
        
        if not points:
            return 0
        
        points.sort(key = lambda x: x[1])
        count = 1
        
        pre = points[0][1]
        
        for l, r in points: # 也可以写points[1:]，因为起点设为points[0][1]了
            if pre < l:
                count += 1
                pre = r
        return count
    
        """
        for loop 另一种写法
        for p in points/points[1:]:
            if pre < p[0]:
                count += 1
                pre = p[1]
        """