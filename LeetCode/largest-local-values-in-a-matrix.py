class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        new_mat = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                max_ele = 0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        max_ele = max(max_ele,grid[k][l])
                new_mat[i][j]+=max_ele
        return new_mat
                