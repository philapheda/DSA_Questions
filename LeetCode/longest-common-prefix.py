class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_str, max_str = min(strs), max(strs)
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str  