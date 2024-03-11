n = int(input())
x = 65
cnt = 0

for i in range(n):
    for j in range(n):
        print(chr(x + cnt), end="")
        cnt += 1
    print()