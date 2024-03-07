n = int(input())

# *
# * * *
# * *
# * *
# * * *
# *

for i in range(1, n + 1):
    for _ in range(i):
        print("*", end=" ")
    print()
    for _ in range(n + 1 - i):
        print("*", end=" ")
    print()