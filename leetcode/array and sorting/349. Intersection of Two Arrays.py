class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        d = {}
        tmp = []
        re = []
        
        for num in nums1:
            if num not in d:
                d[num] = num
        
        for num in nums2:
            if num in d:
                tmp.append(num)
                
        for num in tmp:
            if num not in re:
                re.append(num)
            
        
        return re
        
        # not too hard
        
        """
        python神仙解法
        a, b = set(nums1), set(nums2)
        return a & b
    
        """