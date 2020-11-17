class Solution:
    def frequencySort(self, s: str) -> str:
        
        # 计数器
        # Given a string, 根据character出现频率从大到小排序，区分大小写
        """
        Input:
        "Aabb"

        Output:
        "bbAa"
        
        """   

        ct = sorted(Counter(s).items(), key = lambda x: -x[1])
        
        # print(ct)
        # ct结果是[('e', 2), ('t', 1), ('r', 1)]

        
        res = ""
        for k, v in ct:
            res += k * v
            
        return res
    
        