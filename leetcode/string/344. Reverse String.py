class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # index从两边向中间靠拢，左右的值

        l = 0
        r = len(s) - 1
        
        while l <= r: # <=或者<都可以
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
        
        
        
        """
        built-in function solutioin
        s.reverse()
        return s
        """