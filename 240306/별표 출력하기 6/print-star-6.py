n = int(input())

for i in range(n):
    for j in range(2 * i):
        print(" ", end="")
    for k in range(3 + n - i * 2):
        print("*", end=" ")
    print()

for i in range(n - 2, -1, -1):
    for j in range(2 * i):
        print(" ", end="")
    for k in range(3 + n - i * 2):
        print("*", end=" ")
    print()