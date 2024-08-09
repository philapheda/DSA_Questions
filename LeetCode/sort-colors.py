class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]>nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]          
        """
        Do not return anything, modify nums in-place instead.
        """
        