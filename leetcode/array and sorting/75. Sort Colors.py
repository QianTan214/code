class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """one-pass algorithm method, 用三个指针 and swap values
        if if .. 每个if都会判断一下，if else则相互互斥，只执行其中一个
        
        """

        l = 0
        m = 0
        r = len(nums) - 1
        
        while m <= r:
            if nums[m] == 0 and l < m:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
            else:
                m += 1
        return nums
        # 好好看一下，三个指针和swap value in-place的用法
        
        
        
        """
        two-pass algorithm method
        x = 0
        y = 0
        z = 0
        
        for num in nums:
            if num == 1:
                x += 1
            elif num == 2:
                y += 1
            else:
                z += 1
        
        for i in range(z):
            nums[i] = 0
        for i in range(z, z + x):
            nums[i] = 1
        for i in range(z + x, z + x +y):
            nums[i] = 2
            
        return nums
        
        
        """
      