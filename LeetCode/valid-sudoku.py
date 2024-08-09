class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in count:
                        return False
                    count.add(board[i][j])

        for i in range(9):
            count = set()
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in count:
                        return False
                    count.add(board[j][i])               
        for i in range(0,9,3):
            for j in range(0,9,3):
                count = set() 
                for k in range(j,j+3):   
                        for l in range(i,i+3):
                            if board[l][k].isdigit():
                                if board[l][k] in count:
                                    return False
                                count.add(board[l][k])
        return 1

