class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Python中除了”“、0、()、[]、{}、None为False之外，其他的都是True
        
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0
        
        
        
        """
        can not figure out why below does not work, maybe because the question
        askes not to make a copy of the array
                
        count = 0
        
        for num in nums:
            if num == 0:
                nums.remove(num)
                count += 1
        
        for i in range(count):
            nums.append(0)
        return nums
            
        """
        
        
        """
        神仙解法
        nums.sort(key=bool, reverse=True)
        
        """
        
        
        