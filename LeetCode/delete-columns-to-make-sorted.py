class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        row, col = len(strs), len(strs[0])
        mat = mat = [[""] * row for i in range(col)]
        for i in range(col):
            for j in range(row):
                mat[i][j] +=  strs[j][i]
        count = 0
        for i in mat:
            if i != sorted(i):
                count+=1
        return(count)