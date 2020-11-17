class Solution:
    def maxPower(self, s: str) -> int:
    
        
        res = count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
                
        return res