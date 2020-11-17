class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        result = ""
        count = 0
        n = str(n)
        
            
        for i in range(len(n)-1, -1, -1): # 反向loop through每个元素
            if count < 3:
                result = n[i] + result # 顺序不能反
                count += 1
            if count == 3 and i >= 1: # 注意这一点
                result = "." + result 
                count = 0
        return result
                
        # 在每个千分位加"."和string + 的用法       
            
            
            
           
        