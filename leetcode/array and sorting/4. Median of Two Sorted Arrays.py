class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 求两个array merge后的media value
        # 要求用O(log (m+n))


        nums = nums1 + nums2
        nums.sort()
        
        if not nums:
            return None
        
        n = len(nums)
        
        for num in nums:
            if n % 2:
                return nums[(n-1) // 2] # 注意这里n为奇数时index算法
            else:
                return (nums[n//2 - 1] + nums[n//2]) / 2
        
            