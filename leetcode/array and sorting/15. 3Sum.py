class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                    
        
        nums.sort()
        result = []
        n = len(nums)
        
        if n < 3:
            return result
        
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
                       
            l = i + 1
            r = n - 1
              
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp > 0:
                    r -= 1
                if tmp < 0:
                    l += 1  
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1 
                        
        return result
        
        """
        利用for loop i固定，l 和 r 分别往右和往左移动，三个数相加为0，则append到[]中
        不能有重复elements，通过两个while语句，把l 和 r分别向左右移动跳过重复元素
        如 -4 -1 -1 -1 0 1 2 2 2 4
        """

        """
        there is no a set of list
        can do a set of tuples
        
        """
        
       