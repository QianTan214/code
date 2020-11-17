class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        """
        n个石子，每人每次只能拿完全平方数个，谁最后那谁赢  
        
        """


        # 1 2 3 4 5 6 7 8 9 10
        # T F T T F T F T T F


        dp= [False] * (n+1)
        
        for i in range(1, n+1):
            j = 1
            while j * j <= i: # 遍历所有小于等于i的完全平方数
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]