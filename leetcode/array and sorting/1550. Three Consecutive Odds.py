class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        count = 0
        re = 0
        
        for i in arr:
            re = max(re, count)
            if i % 2 == 1:
                count += 1
            else:
                count = 0
        if max(re,count) >= 3: # 这里和485题很像
            return True
        return False
        

       # too easy         
        
        
        """
        
        count = 0
        
        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True
        return False
        
        """
            