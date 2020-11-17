class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1
              
        # 运用count，nums[count]=nums[i]解题
        # 替换array中元素
        # 值得review
        
        """
        can not pass test, have to use in-place algorithm
        nums = list(set(nums))
        nums.sort()
        return len(nums)
        
        """
        
        
        
       