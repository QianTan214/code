class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max_subset = -float("inf")
       
      
        for num in nums:
            if num + max_subset <= num:
                max_subset = num
            else:
                max_subset = num + max_subset
            
            result = max (max_subset, result)
        return result
            

    
    """
   
            nums:        -2, 1, -3, 4,-1, 2, 1,-5, 4
            max_subset:  -2, 1, -2, 4, 3, 5, 6, 1, 5
            result:   6
    """
    
    