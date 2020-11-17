class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # 贪心
        # 删除被包含区间

        intervals.sort(key = lambda x: (x[0], -x[1])) #按左端点升序，右端点降序排序
        remains = 0
        pre = 0
        
        for _, r in intervals: # underscore的用法, 也可以用l代替，不过后面l用不到
            if r > pre:
                remains += 1
                pre = r
        return remains
                
        