class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # 二分法
        """
        判断一个数是不是完全平方数，不可以用sqrt函数

        Input: num = 16
        Output: true
        """
        
        l = 1
        r = num
        
        while l <= r:
            m = (l + r) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 > num:
                r = m - 1
            else:
                l = m + 1
        return False
            