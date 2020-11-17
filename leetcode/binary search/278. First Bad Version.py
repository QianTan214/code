# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        找到第一个坏版本号出现的位置
        """

        # 二分法
        
        l = 1
        r = n
        
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m): # isBadVersion function给定了
                r = m
            else:
                l = m + 1
        return l
    
    # 例如：GGGGBBB
        
            