class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_element = -1
        a = tuple(arr)
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                max_element = max(max_element,a[i+1])
                arr[i] = max_element
        return arr 