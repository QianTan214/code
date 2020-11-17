class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        l = 0
        r = len(numbers) - 1
        sum = 0
        
        while l != r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            elif sum == target:
                return [l+1, r+1]
                
        # 从两边往中间的思想
        
        
        """
        time out solution
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        """