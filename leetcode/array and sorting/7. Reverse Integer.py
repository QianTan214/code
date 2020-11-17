class Solution:
    def reverse(self, x: int) -> int:
              
        a = abs(x)
        num = 0
        while a != 0:
            tmp = a % 10
            num = num * 10 + tmp
            a = a // 10
        
        if x > 0:
            if num <= 2**31 - 1:
                return num
            return 0
        elif x < 0:
            if -num >= -2**31:
                return -num
            return 0
        else:
            return 0
        
        """
        int范围-2^31到2^31-1

        值得review
        """