arr = list(map(int, input().split()))
x = []

for e in arr:
    if e == 0:
        break
    else:
        x.append(e)

for e in x:
    if e % 2 == 0:
        print(e // 2, end=" ")
    else:
        print(e + 3, end=" ")