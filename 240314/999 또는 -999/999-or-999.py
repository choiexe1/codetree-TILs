n = list(map(int, input().split()))
x = []

for e in n:
    if e == 999 or e == -999:
        break
    else:
        x.append(e)

print(max(x), min(x))