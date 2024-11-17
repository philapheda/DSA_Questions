class Solution(object):
    def pancakeSort(self, arr):
        def flip(arr1,k):
            start = 0
            end = k-1
            while start < end:
                arr1[start],arr1[end] = arr1[end],arr1[start]
                start+=1
                end-=1
            return arr1
        j = len(arr)
        ans = []
        while arr != sorted(arr):
            for i in range(len(arr)):
                if arr[i] == j:
                    arr = flip(arr,i+1)
                    arr = flip(arr,j)
                    ans.append(i+1)
                    ans.append(j)
                    j-=1
        return ans

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        