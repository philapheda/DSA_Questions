class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        n = len(nums)
        i = 0
        j = 0
        while j<n:
            if nums[j] == 0:
                j = j+1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i = i+1
                j = j+1  
        return nums             
        