class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # 求最少删除几个区间使得剩下的区间都不重合 

        """
        Input: [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of intervals are non-overlapping. 

        """


        if not intervals: # 区间是空返回0
            return 0
        
        intervals.sort()
        
        count = 0
        pre = intervals[0][1]
        
        for l, r in intervals[1:]:
            if l < pre:
                count += 1
                pre = min(pre, r) # 注意这个不能漏，取右端点比较小的
            else:
                pre = r
        return count
            