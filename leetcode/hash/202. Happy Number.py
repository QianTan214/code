class Solution:
    def isHappy(self, n: int) -> bool:

        """
        Input: 19
        Output: true

        Explanation: 
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
        """

        s = {n}
        while n != 1:
            res = 0
            while n != 0:
                res += (n % 10) ** 2
                n = n // 10
            if res in s:
                return False
            s.add(res)
            n = res
        return True
            
            
                
                    
            