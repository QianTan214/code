"""
recursive

fibonacci sequence 

overlapping sub-problem: 重叠子问题，low efficiency, 重复计算
解决方法：通过数组保存已经有的值，就不用重复计算了

"""


# 动态规划，求最大值

OPT(i) = max(选第i个/不选第i个)
选：vi + OPT(prev(i))
不选：OPT(i - 1)




