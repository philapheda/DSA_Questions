class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        a = sorted(list(set(nums)))
        b = Counter(nums)
        count = 0
        for i in range(len(a)):
            count+=i*b[a[i]]
        return count