"""
arr = [1 2 4 1 7 8 3]
求不相邻的数能组成的最大的和

OPT(6)代表到index为6 (即3)的最佳方案


选和不选：比较下面两种哪个大

# 递归方程
选：arr[i] + OPT(i-2)
不选：OPT(i-1)

# 递归出口
OPT(0) = arr[0]
OPT(1) = max (arr[0], arr[1])


"""

# arr = [1 2 4 1 7 8 3]
# 用DP方式写的代码
# 创建一个数组opt，长度等于原array

# 要用numpy
import numpy as np 

arr = [1, 2, 4, 1, 7, 8, 3]

def dp_opt(arr):
    opt = np.zeros(len(arr)) # 创建一个数值都为0的array
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    return opt [len(arr) - 1]

C = dp_opt(arr)
print(C)

# 结果15.0