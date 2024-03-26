a, b, x = [], [], [[0 for _ in range(3)] for _ in range(3)]

for _ in range(3):
    i = list(map(int, input().split()))
    a.append(i)
input()
for _ in range(3):
    i = list(map(int, input().split()))
    b.append(i)

for i in range(3):
    for j in range(3):
        x[i][j] = a[i][j] * b[i][j]

for row in x:
    for e in row:
        print(e, end=" ")
    print()