class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        """
        method 1: XOR 亦或算法，符合交换律
        a ^ a = 0
        a ^ 0 = a

        """
        re = 0
        
        for num in nums:
            re ^= num
            
        return re
        

        """
        method 2: 用reduce函数
        functools.return reduce(lambda x, y: x ^ y, nums)
        
        """
        
        
        """
        method 3: 计数器
        ct = Counter(nums)
        
        for k, v in ct.items():
            if v == 1:
                return k
        """
        
        
        """
        method 4: count()
        slow solution
        for num in nums:
            if nums.count(num) == 1:
                return num
        """      
        
      