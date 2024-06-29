class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        new_mat = []
        soln = [[0]*c for _ in range(r)]
        if row*col != r*c:
            return mat
        else:
            for i in range(row):
                for j in range(col):
                    new_mat.append(mat[i][j])
            for i in range(r):
                for j in range(c):
                    soln[i][j]+=new_mat[i*c+j]
            return soln