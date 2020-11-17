""" 二分查找 binary search"""


要求排过序，要求有索引，所以只能应用于list不能应用于linked list

最优 O(1)
最坏 O(Logn)



""" 二分查找代码实现(递归) """


def binary(nums, val):
    n = len(nums)
    if n > 0:
        mid = n//2
        if nums[mid] == val:
            return True
        elif val < nums[mid]:
            return binary(nums[:mid], val)
        else:
            return binary(nums[mid+1:], val)
    return False


l = [17, 20, 26, 31, 44, 54, 55, 77, 93]   
print(binary(l, 55))
print(binary(l, 100))




""" 二分查找代码实现(非递归) """

def binary(nums, val):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == val:
            return True
        elif nums[m] > val:
            r = m - 1
        else:
            l = m + 1
    return False