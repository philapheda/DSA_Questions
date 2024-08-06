t = int(input())
for i in range(t):
    max_val = 0
    n,m = map(int, input().split())
    mat = []
    for j in range(n):
        mat.append(list(map(int, input().split())))
    for k in range(n):
        for l in range(m):
            a = k
            b = l
            diagonals = []
            while a<n and b<m:
                diagonals.append(mat[a][b])
                a+=1
                b+=1
            a = k
            b = l            
            while a>0 and b>0:
                diagonals.append(mat[a-1][b-b])
                a-=1
                b-=1
            a = k
            b = l
            while a>0 and b == 0:
                diagonals.append(mat[a-1][b+1])
                a-=1
                b+=1
            a = k
            b = l
            while a==0 and b > 0:
                diagonals.append(mat[a+1][b-1])
                b-=1
                a+1            
            print(diagonals)
