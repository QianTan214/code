class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        
        for i in range(len(haystack) - len(needle) + 1): # 范围要弄明白
            if haystack[i : i+len(needle)] == needle:
                return i
                
        return -1
  

        """
        bool("") - False
        "A" in "" - Flase
        "" in "A" -True
        len("") = 0
        len(" ") = 1
        
        """