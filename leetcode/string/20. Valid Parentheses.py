class Solution:
    def isValid(self, s: str) -> bool:
        
        
        d = {"[" : "]", "{" : "}", "(": ")"} 
        ls = []
        
        for char in s:
            if char in d:
                ls.append(char)
            else:
                if len(ls) == 0 or d[ls.pop()] != char:
                    return False
        
        if len(ls) == 0:
            return True
        
        # 也可写成return len(ls) == 0，等价

        # dict的运用
        # 把 or 两边对调就出错了，不知道为什么？？？？？？？？
      
     
     
      