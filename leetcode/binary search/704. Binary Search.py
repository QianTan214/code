class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 二分法
        """
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4

        Explanation: 9 exists in nums and its index is 4
        
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
        return -1