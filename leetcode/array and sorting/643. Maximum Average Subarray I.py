class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        tmp = 0
        result = float("-inf")
        
        for i, num in enumerate(nums):
            tmp += num
            if i >= k:
                tmp = tmp - nums[i-k]
            if i >= k-1:
                if tmp > result:
                    result = tmp
            
        return result/k
    
        # 好题，做法值得review
        # 搞清楚for loop里语句执行关系
                
        
        
       