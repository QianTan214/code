class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # have to consider uppercase and lowercase vowels
        # 需要用lower()
        # 和344题比较像
        
        s = list(s)
        l = 0
        r = len(s) - 1
        lst = ["a","e","i","o","u"]
        
        
        while l < r:
            if s[l].lower() not in lst:
                l += 1
            if s[r].lower() not in lst:
                r -= 1
            if s[l].lower() in lst and s[r].lower() in lst:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            
        return "".join(s)