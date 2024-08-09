class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[0])):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col] 
        for i in matrix:
            i.reverse()
        """
        Do not return anything, modify matrix in-place instead.
        """
        