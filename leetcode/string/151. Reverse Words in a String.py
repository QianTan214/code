class Solution:
    def reverseWords(self, s: str) -> str:
        
        # 我的解法

        l = s.split() # split(" ")去除一个空格，split()去除所有空格
        # print (l)
        
        l.reverse()
        
        result = ""
        
        for i in range(len(l) - 1):
            result = result + l[i] + " "
        
        result = result + l[-1]
        
        return result
        
        """
        评论区神仙解法
        s = s.split()
        s.reverse()
        return ' '.join(s) 

        """
        # .join()把list转换成string，split把string转换成list