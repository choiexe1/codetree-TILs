n = int(input())

for i in range(n):
    if n == 1:
        print(1)
    for j in range(1, n * n, n):
        print(i + j, end=" ")
    print()