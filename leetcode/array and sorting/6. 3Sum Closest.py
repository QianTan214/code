class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[n-1]
        
        for i in range(n-2):
            
            l = i + 1
            r = n - 1
            
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(tmp-target) < abs(result-target):
                    result = tmp
                               
                if tmp == target:
                    return target
                
                elif tmp > target:
                    r -= 1
                
                else:
                    l += 1  
     
        return result
    
        
        """
        can not figure out why below does not work
        
        nums.sort()
        d={}
        n = len(nums)
        #result = float("inf")
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                diff = abs(sum-target)
                if diff not in d:
                    d[diff] = sum
                
                #result = min(result, diff)
                
                if sum == target:
                    return target
                
                elif sum > target:
                    r -= 1
                
                else:
                    l += 1
        
        for k, v in d.items():
            if k == min(d.keys()):
                v = d[k]
        
        return v
              
        """