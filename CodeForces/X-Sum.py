for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for _ in range (n):
        row = list(map(int, input().split()))
        matrix.append(row)
    max_sum = 0
    for i in range(n):
        for j in range(m):
            curr_sum = matrix[i][j]
            x, y = i + 1 , j + 1
            while x < n and y < m:
                curr_sum += matrix[x][y]
                x+=1
                y+=1
            x, y = i-1 , j-1
            while x >= 0 and y >= 0:
                curr_sum += matrix[x][y]
                x-=1
                y-=1
            x, y = i-1 , j+1
            while x >= 0 and y<m:
                curr_sum += matrix[x][y]
                x-=1
                y+=1
            x, y = i+1 , j-1
            while x < n and y >= 0:
                curr_sum += matrix[x][y]
                x+=1
                y-=1
            max_sum = max(curr_sum, max_sum)
    print(max_sum)