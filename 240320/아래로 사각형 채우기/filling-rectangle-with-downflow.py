n = int(input())

for i in range(n):
    for j in range(1, n * n, n):
        print(i + j, end=" ")
    print()