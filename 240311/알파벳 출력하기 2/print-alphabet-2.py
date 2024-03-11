n = int(input())
c = 65

for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        if chr(c) == '[':
            c = 65
        print(chr(c), end=" ")
        c += 1
    print()