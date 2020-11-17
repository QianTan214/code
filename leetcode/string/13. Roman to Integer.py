class Solution:
    def romanToInt(self, s: str) -> int:
        
        # staightforward解法
        s=s.replace('IV','A')
        s=s.replace('IX','B')
        s=s.replace('XL','F')
        s=s.replace('XC','Z')
        s=s.replace('CD','E')
        s=s.replace('CM','G')
        
        d = { 'I':1, 'V':5, 'X':10,'L':50, 'C': 100,'D':500,'M':1000, 'A':4,'B':9,'F':40, 'Z':90,'E':400,'G':900}

        
        return sum([d[char] for char in list(s)])
        
        
        
        """
        youtube解法，没完全明白
        d = {"I": 1, "V": 5, "X" : 10, "L" : 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        
        for i in range(len(s)):
            if i > 0 and d[s[i]] > d[s[i-1]]:
                num += d[s[i]] - 2 * d[s[i-1]] 
            else:
                num += d[s[i]]
                
        return num
        """