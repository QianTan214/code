class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        r = 0
        for i in range(len(nums)):
            if i + nums[i] >= r: # 等价r = max(r, i+nums[i])
                r = i + nums[i]
            if r >= len(nums)-1:
                return True
            if i == r and nums[i] == 0:
                return False
        
        
        
        """
        youtube 解法
        reach = 0
        for i, n in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach,i+n)
        return True
        """