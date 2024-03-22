n, m = tuple(map(int, input().split()))
x = [[0 for _ in range(m)]
    for _ in range(n)
]

count = 0

for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            x[row][col] = count
            count += 1
    else:
        for row in range(n - 1, -1, -1):
            x[row][col] = count
            count += 1

for row in x:
    for e in row:
        print(e, end=" ")
    print()