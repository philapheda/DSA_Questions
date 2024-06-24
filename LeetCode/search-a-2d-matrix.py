class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in matrix:
            if target <= i[m-1]:
                if target in i:
                    return True
                else:
                    return False