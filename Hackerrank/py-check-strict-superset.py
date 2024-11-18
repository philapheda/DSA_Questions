superset = set(map(int, input().split()))
n = int(input())
is_strict_superset = True
for i in range(n):
    subset = set(map(int, input().split()))
    if not (superset > subset):
        is_strict_superset = False
        break
print(is_strict_superset)