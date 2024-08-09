class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        soln = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                soln.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return soln
