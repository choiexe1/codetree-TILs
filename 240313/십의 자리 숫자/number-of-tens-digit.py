n = list(map(int, input().split()))
x = [0 for _ in range(9)]

for e in n:
    if e == 0:
        break
    if e // 10 > 0:
        x[e // 10 - 1] += 1

for i in range(len(x)):
    print(f"{i + 1} - {x[i]}")