class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if abs(i - d[nums[i]]) <= k:
                    return True
                d[nums[i]] = i # 直接写 d[nums[i]] = i和if并列，不用写elif语句,可以写但麻烦
                        
        return False  
        
        
        
        
        """
        time out solution
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False
        """