class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # 比较多个string最长的common prefix
        # 还有一种用二维数组的方法

        result = ""
        
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop() # set.pop()用法
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result

        """
        用set解题
        
        """