def shell (nums):
    n = len(nums)
    gap = n // 2

    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if nums[i] < nums[i-gap]:
                    nums[i],nums[i-gap] = nums[i-gap], nums[i]
                    i -= gap
                else:
                    break
        gap //= 2

nums = [54,26,93,17,77,31,44,55,20]
print(nums)
shell(nums)
print(nums)
