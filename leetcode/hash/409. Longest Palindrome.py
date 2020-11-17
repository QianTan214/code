class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # 计数器
        # 求一个string里能组成的最长回文串的长度
        # 所有出现偶数次的字母都能用，出现基数次先减一变成偶数次
        """
        Input: s = "abccccdd"
        Output: 7

        Explanation:
        One longest palindrome that can be built is "dccaccd", whose length is 7.
        """
        ct = Counter(s)
        res = 0
        tmp = 0
        
        for v in ct.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                tmp = 1
        if tmp == 1:
            return res 
        else:
            return res + 1
        
                
            
