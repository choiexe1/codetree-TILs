n, m = map(int, input().split())

x = [[0 for j in range(1, m + 1)]
        for i in range(n)]

count = 1

for row in x:
    for e in row:
        print(e + count, end=" ")
        count += 1
    print()