from collections import defaultdict
n,m = map(int, input().split())
groupa = defaultdict(list)
groupb = []
for i in range(n):
    a = input()
    groupa[a].append(i)
for j in range(m):
    a = input()
    groupb.append(a)
for k in groupb:
    if k in groupa:
        for i in groupa[k]:
            print(i+1, end = " ")
        print()
    else:
        print(-1)