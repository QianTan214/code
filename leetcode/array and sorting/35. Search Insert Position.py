class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        """
        Input: nums = [1,3,5,6], target = 2
        Output: 1

        """


        """
        method 1: 二分法
        """
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
        

        """
        method 2: 用bisect函数
        """ 

        return bisect.bisect_left(nums, target)
               
        
        
        """
        method 3: 遍历
        """

        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        
         