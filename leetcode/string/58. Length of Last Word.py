class Solution:
    def lengthOfLastWord(self, s: str) -> int:
     
              
        count = 0
        result = 0
        
        for i in range(len(s)):
            if s[i] == " ":
                count = 0
            else:
                count += 1
                result = count # 这条语句就是"hello  "后有空格这种情况，把count存在result里
        return result
                
        # 此题要注意"hello  "这种情况,hello后面有空格
      
        
        """
        s = "a"
        s[0] = s[-1] = a
        
        """
        
        
        
        