class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        # 判断一个整数是否是palindrome回文串
        
        """
        method 1: reverse integer
        
        """
        
        if x < 0:
            return False
        if x == 0:
            return True
        
        res = x
        num = 0
        while x != 0:
            tmp = x % 10
            num = num * 10 + tmp 
            x = x // 10
            
        if res == num:
            return True
        return False
        

        """
        method 2: convert int to string
        
        """
        
        if x < 0:
            return False
        if x == 0:
            return True
        
        x = str(x) # 先转成string，才能用len(x)，int没有len()
        l = 0
        r = len(x) - 1

        for i in x:
            while l <= r:
                if x[l] == x[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        
                    
            
            
        