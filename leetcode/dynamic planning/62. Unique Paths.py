class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        # method1: 组合数学
        
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
        
    
        # method 2: 动态规划
        
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]