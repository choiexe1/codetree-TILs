a, b = map(int, input().split())

if a % 1 == 0:
    for i in range(b):
        print(a, end="")
else:
    print(0)