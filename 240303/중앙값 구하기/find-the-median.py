a, b, c = map(int, input().split())
min = min(a, b, c)
max = max(a, b, c)

for i in [a, b, c]:
    if i != min and i != max:
        print(i)