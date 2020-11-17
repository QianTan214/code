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
# 在数组arr中，找出一组不相邻的数字，使得最后的和最大
# arr = [1 2 4 1 7 8 3]
# 用递归方式写的代码
# 会有重叠子问题，运行慢

arr = [1, 2, 4, 1, 7, 8, 3]

def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i-1)
        return max(A, B)

C = rec_opt(arr, 6)
print(C)

# 结果15