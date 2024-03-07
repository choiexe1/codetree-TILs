n = int(input())
x, y = 1, 4


for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            print(x, end="")
            x += 1
        else:
            print(y, end="")
            y -= 1
    x = 1
    y = 4
    print()