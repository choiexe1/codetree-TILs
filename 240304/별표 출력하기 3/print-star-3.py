n = int(input())


for i in range(n, -1, -1):
    for _ in range((2 * n) - (2 * i )):
        print(" ", end="")
    for j in range((2 * i) - 1):
        print("*", end=" ")
    print()