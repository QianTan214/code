class Solution:
    def addDigits(self, num: int) -> int:
                
        """
        非负整数各个位数相加直到结果为个位数

        """

        while num >= 10:
            total = 0
            for i in range (len(str(num))):
                total = total + int(str(num)[i])
            num = total
        return num
        
        
        """
        不懂逻辑
        n = num
        
        while n//10 != 0:
            n = n // 10 + n % 10
    
        return n
        """