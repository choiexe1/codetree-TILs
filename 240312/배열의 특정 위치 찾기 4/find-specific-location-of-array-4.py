arr = list(map(int, input().split()))
x = []

for e in arr:
    if e == 0:
        break
    else:
        x.append(e)

count = 0
sum = 0

for e in x:
    if e % 2 == 0:
        count += 1
        sum += e

print(f"{count} {sum}")