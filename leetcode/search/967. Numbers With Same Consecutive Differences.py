class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        """
        Input: n = 3, k = 7
        Output: [181,292,707,818,929]
        Explanation: Note that 070 is not a valid number, because it has leading zeroes.

        """


        if n == 1:
            return range(10)
        
        q =range(1, 10) # 如果n大于1，遍历1-9
        
        for i in range(n - 1):
            tmp = [] # 存bfs下一次所有结果
            for n in q:# 遍历q中1-9
                for d in set([n % 10 + k, n % 10 - k]): # k = 0时，两个重复，用set去重
                    if 0 <= d <10:
                        tmp.append(n * 10 + d)
            q = tmp
        return q