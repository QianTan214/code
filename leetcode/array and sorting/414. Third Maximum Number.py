class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       
        
        nums = set(nums)
        
        if len(nums) < 3:
            return max(nums)
        else:
            nums.discard(max(nums))
            nums.discard(max(nums))
        
        return max(nums)
    
        # not too hard
        # 求第几大时可先排序，如第三大，则nums[-3]
    
        """
        youtube solution
        
        nums = list(set(nums))
        nums.sort()
    
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
        
        """
    