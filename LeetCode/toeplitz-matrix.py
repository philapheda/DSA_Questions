class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        dic = {}
        for i in range(row):
            for j in range(col):
                k = i-j
                if (k in dic):
                    if (dic[k] != matrix[i][j]):
                        return False
                else:
                    dic[k] = matrix[i][j]
        return True
