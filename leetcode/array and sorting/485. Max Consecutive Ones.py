class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        count = 0
        re = 0
        
        for num in nums:
            
            if num == 1:
                count += 1
            else:
                re = max(count, re)
                count = 0
       
                
        return max(count, re) 
    
    """
    要注意这里，假设最后一位是1，只是count加一了，并没有更新结果，所以要找到count和re其中更大的
    
    """