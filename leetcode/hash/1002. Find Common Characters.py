class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        计数器
        找common character，如有重复，取最小值

        Input: ["cool","lock","cook"]
        Output: ["c","o"]

        """
        # from collections import Counter
        ct = Counter(A[0])

        for w in A[1:]:
            tmp = Counter(w)
            for key in list(ct.keys()): #要转换成list
                if key not in tmp:
                    del ct[key]
                else:
                    ct[key] = min(ct[key], tmp[key])
        res = []
        for key in ct:
            res += [key] * ct[key] # +号生成的是一个新对象，而extend是在原地修改第一个list对象
        return res
            

        
            


            
           