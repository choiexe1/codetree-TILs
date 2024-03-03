a, b = map(int, input().split())
n = a
for i in range(a, b + 1):
    if n > b:
        break
    print(n, end=" ")
    if i % 2 == 0:
        n += 3
    elif i % 2 != 0:
        n = n * 2