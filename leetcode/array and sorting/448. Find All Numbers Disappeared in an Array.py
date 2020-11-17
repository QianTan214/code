class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #if not nums:
         #   return []
        
        re = []
        n = len(nums) # calculate length of list nums before converting it into a set
        nums = set(nums)

        for i in range(1, (n + 1)):
            if i not in nums:
                re.append(i)
        return re

        # not too hard