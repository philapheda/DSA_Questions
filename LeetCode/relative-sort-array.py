class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = Counter(arr1)
        ans = []
        for i in arr2:
            if i in arr1:
                for j in range(arr1[i]):
                    ans.append(i)
                del arr1[i] 
            else:
                ans.append(i)
        arr1 = dict(sorted(arr1.items()))
        for i in arr1:
            for j in range(arr1[i]):
                ans.append(i)
        return ans  