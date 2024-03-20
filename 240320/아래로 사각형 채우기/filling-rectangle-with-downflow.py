n = int(input())

for i in range(n):
    for j in range(1, n * 5, 5):
        print(i + j, end=" ")
    print()