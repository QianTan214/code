class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        """
        method 1：看长度
        """

        if not s:
            return True # empty string is always a sub of non-empty string  
        
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
                    
        # 比较字符串，loop through 大的string t


        """
        method 2: 找到一个删除一个
        """
        s = list(s)

        for c in t:
            if not s: # 为什么这句必须写在for里，写在上面就不对？？？？？？？？？
                return True
            if c == s[0]:
                s.pop(0)
        
        return not s # s最后为空，则是subsequence
        
        