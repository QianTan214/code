""" bubble sort """

index依次向后移动，比较当前游标所指数值和下一个数值大小

最优O(n)
最坏O(n^2)
稳定

""" bubble sort 代码 """


def bubble (nums):
    n = len(nums)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

nums = [54,26,93,17,77,31,44,55,20]
print(nums)
bubble(nums)
print(nums)



""" bubble sort 代码优化 """

def bubble (nums):
    n = len(nums)
    for j in range(n - 1):
        count = 0
        for i in range(n - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                count += 1
        if count == 0:
            return nums


# nums = [1,2,3,4,5,6]
nums = [54,26,93,17,77,31,44,55,20]
print(nums)
bubble(nums)
print(nums)


""" selection sort """


index依次向后移动，比较当前游标所指数值和下一个数值大小

最优O(n^2)
最坏O(n^2)
不稳定

""" selection sort 代码 """

# selection sort是交换索引
# 先写内部代码，再看外层需要执行多少次

def selection(nums):
    n = len(nums)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if nums[min_index] > nums[i]:
                min_index = i
        nums[j], nums[min_index] = nums[min_index], nums[j]
    

# nums = [1,2,3,4,5,6]
nums = [54,26,93,17,77,31,44,55,20]
print(nums)
selection(nums)
print(nums)






""" insertion sort 代码 """

最优O(n)
最坏O(n^2)
稳定



""" selection sort 代码 """

def insertion (nums):
    n = len(nums)
    for j in range(1,n):
        i = j
        while i > 0:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
            else:
                break





""" shell sort希尔排序 """

insertion sort的演变

按照步长gap大小分为子序列，然后按照insertion sort排序

最坏O(n^2)
不稳定
gap = 1，就是insertion sort

""" shell sort希尔排序代码实现 """


def shell (nums):
    n = len(nums)
    gap = n // 2

    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if nums[i] < nums[i-gap]:
                    nums[i], nums[i-gap] = nums[i-gap], nums[i]
                    i -= gap
                else:
                    break
        gap //= 2 # gap取半，也可以取其他的


