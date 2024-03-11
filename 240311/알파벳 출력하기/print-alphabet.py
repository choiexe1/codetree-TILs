n = int(input())
c = 65

for i in range(1, n + 1):
    for j in range(i):
        if chr(c) == '[':
            c = 65
        print(chr(c), end="")
        c += 1
    print()