class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        

        """
        Write a function to find all the 10-letter-long sequences (substrings) 
        that occur more than once in a DNA molecule.
        
        """
        seen, res = set(), set()
        
        for i in range(len(s) - 9):
            tmp = s[i:i+10] # 每次取十个
            if tmp not in seen:
                seen.add(tmp)
            else:
                res.add(tmp)
        return res

        # 用Rabin-Karp算法解 看1044题