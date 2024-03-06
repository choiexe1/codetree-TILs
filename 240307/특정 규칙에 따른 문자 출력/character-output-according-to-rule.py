n = int(input())

for i in range(n):
    for j in range(n + 1 - (2 * i)):
        print(" ", end="")
    for k in range(i + 1):
        print("@", end=" ")
    print()


for i in range(n - 2, -1, -1):
    # for j in range(n + 1 - (2 * i)):
    #     print(" ", end="")
    for k in range(i):
        print("@", end=" ")
    print()


# 3
# 0, 4
# 1, 2
# 2, 0