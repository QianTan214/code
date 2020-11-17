class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # 动态规划
        dp1, dp2 = 1, 2
        
        for i in range(n - 1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp1
        
        
        
        
        """
        pre, cur = 0, 1
        
        for i in range(n):
            pre, cur = cur, pre + cur
        return cur
        
        # n = 1: 1
        # n = 2: 2
        # n = 3: 3
        # n = 4: 5
        # n = 5: 8
        # ... Fibonacci
        
        """
        
     