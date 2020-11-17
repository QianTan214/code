class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # 计数器
        """
        找第一个不重复出现的字符

        s = "leetcode"
        return 0.

        s = "loveleetcode"
        return 2.

        """

        ct = Counter(s) # from collections import Counter
        
        for i in range(len(s)):
            if ct[s[i]] == 1:
                return i
        return -1
        
            