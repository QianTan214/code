class Solution:
    def titleToNumber(self, s: str) -> int:
        
        # 26进制
        
        # ord("A") = 65
        # chr(97) = "a"
        
        """
        把column title in Excel sheet转换成数字
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
        """

        res = 0
        n = len(s)
        
        for i in range(len(s)):
            res = res + (ord(s[i]) -64) * (26 ** (n - 1 - i))
        return res

        """
        # 或者
        for c in s:
            res = res * 26 + ord(c) - 64
        return res

        """