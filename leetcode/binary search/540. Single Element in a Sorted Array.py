class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        """
        二分法 O(log n)
        值得review
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            
            if (m % 2 == 1 and nums[m] == nums[m-1]) or (m % 2 == 0 and nums[m] == nums[m+1]):
                l = m + 1
          
            else:
                r = m - 1
        return nums[l]
         
        
        """
        
        # 亦或法, O(n)
        res = 0
        for num in nums:
            res = res ^ num
        return res
        
        # Counter法
        ct = Counter(nums)
        for k, v in ct.items():
            if v == 1:
                return k
                
        """