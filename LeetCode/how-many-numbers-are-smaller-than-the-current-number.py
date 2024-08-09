class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a = tuple(nums)
        for i in range(len(nums)):
            k = 0
            for j in range(len(a)):
                if a[i] > a[j]:
                     k+=1        
                nums[i] = k            
        return(nums)    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        