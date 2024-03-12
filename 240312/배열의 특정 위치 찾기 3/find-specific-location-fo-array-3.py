arr = list(map(int, input().split()))
x = []
for e in arr:
    if e == 0:
        break
    else:
        x.append(e)

sum = x[-1] + x[-2] + x[-3]

print(sum)