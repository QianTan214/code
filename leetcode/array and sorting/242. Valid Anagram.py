class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d1 = {}
        
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = 1
            else:
                d1[s[i]] += 1
                
        for i in range(len(t)):
            if t[i] in d1:
                d1[t[i]] -= 1
            else:
                return False
        
        for i in d1:
            if d1[i] != 0:
                return False
        return True
        
        """
        建立一个dict，第一个string出现的话，dict里value加一
        第二个string出现的话，dict里value减一，最后必须所有value都是0，代表key出现次数一样
        
        """