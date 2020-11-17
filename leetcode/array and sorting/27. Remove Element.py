class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
       
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        return count 
        
        
    # 运用count，nums[count]=nums[i]解题
    # 替换array中元素
    # 值得review   
    