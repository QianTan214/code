class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        re = []
        d = {}
        
        for i, num in enumerate(nums):
            if target - num not in d:
                d[num] = i
            else:
                return [i, d[target - num]]
        
        # 字典的用法，值得review
       
            
     