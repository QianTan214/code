class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # 两个字典

        """
        Input: s = "abcd", t = "abcde"
        Output: "e"
        Explanation: 'e' is the letter that was added.
        
        """

        d = defaultdict(int) # defaultdict的用法
        
        for i in s:
            d[i] += 1
        for i in t:
            d[i] -= 1
        for k, v in d.items():
            if v != 0:
                return k