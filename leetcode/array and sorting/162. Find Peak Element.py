class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        size = len(nums)   
        
        for i in range(1, size - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            
        return size - 1 if nums[0] < nums[size - 1] else 0
    
    
    #   return [0, size - 1][nums[0] < nums[size] - 1]  等效, 0 和 size - 1相当于T/F
    
    #   [2, 1] should return 0
    #   [1] should return 0
    #   [1, 2] should return 1