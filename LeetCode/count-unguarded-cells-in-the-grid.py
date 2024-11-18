class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = [[0]*n for _ in range(m)]
        for i in guards:
            x,y = i
            ans[x][y] = 1
        for j in walls:
            x,y = j
            ans[x][y] = 2
        for i in range(m):
            visible = False
            for j in range(n):
                if ans[i][j] == 1:
                    visible = True
                    continue
                elif ans[i][j] == 2:
                    visible = False
                    continue
                if visible:
                    ans[i][j] = 3
        for i in range(m-1,-1,-1):
            visible = False
            for j in range(n-1,-1,-1):
                if ans[i][j] == 1:
                    visible = True
                    continue
                elif ans[i][j] == 2:
                    visible = False
                    continue
                if visible:
                    ans[i][j] = 3
        for i in range(n):
            visible = False
            for j in range(m):
                if ans[j][i] == 1:
                    visible = True
                    continue
                elif ans[j][i] == 2:
                    visible = False
                    continue
                if visible:
                    ans[j][i] = 3
        for i in range(n-1,-1,-1):
            visible = False
            for j in range(m-1,-1,-1):
                if ans[j][i] == 1:
                    visible = True
                    continue
                elif ans[j][i] == 2:
                    visible = False
                    continue
                if visible:
                    ans[j][i] = 3
        count = 0
        for i in range(m):
            for j in range(n):
                if ans[i][j] == 0:
                    count+=1
        return count
        
        