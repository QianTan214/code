class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        

        # 两个字典，映射
        # 找对应关系是否一致
        
        """
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true
        
        """

        s = s.split(" ")
        # print(s)
        
        if len(pattern) != len(s):
            return False
        
        d1 = {}
        d2 = {}
        
        for p, w in zip(pattern, s): # zip的用法
            if p not in d1:
                d1[p] = w
            elif d1[p] != w:
                return False
            if w not in d2:
                d2[w] = p
            elif d2[w] != p:
                return False
        return True