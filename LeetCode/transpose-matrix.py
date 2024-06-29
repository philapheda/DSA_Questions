class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        m = len(matrix[0])
        mat = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                mat[i][j] += matrix[j][i]
        return mat