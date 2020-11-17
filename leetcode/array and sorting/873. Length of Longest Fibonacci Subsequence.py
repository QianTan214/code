class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        """
        2 for loop 确定第一个第二个数
        while loop 确定subsequence多长
        
        """
        
        # 两个loop加一个while的思想
        s = set(A) # convert to set, otherwise timeout， set更快
        n = len(s)
        result = 0
        
        for i in range(n-1):
            for j in range(i+1, n):
                a, b = A[i], A[j]
                count = 2
                while a+b in s:
                    a, b = b, a+b
                    count += 1
                    result = max(result, count)
        if result > 2:
            return result
        else:
            return 0