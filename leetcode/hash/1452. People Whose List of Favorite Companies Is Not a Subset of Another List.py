class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        # 找出不是其他人子集的那个人的index
        # 没有太好的办法，只能遍历每个人
        """
        Input: favoriteCompanies = [["leetcode","google","facebook"],
        ["google","microsoft"],["google","facebook"],["google"],["amazon"]]

        Output: [0,1,4] 
        """
        
        s = [set(f) for f in favoriteCompanies] #转换为set以便用issubset函数
        
        res = []
        
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[i].issubset(s[j]): # i是j的子集
                    break
            else: # 此处else的用法
                res.append(i)
        return res
            
                    
            