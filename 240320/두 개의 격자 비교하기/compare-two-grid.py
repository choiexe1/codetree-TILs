n, m = map(int, input().split())

a, b = [], []

for _ in range(n):
    arr = list(map(int, input().split()))
    a.append(arr)

for _ in range(n):
    arr = list(map(int, input().split()))
    b.append(arr)

for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()