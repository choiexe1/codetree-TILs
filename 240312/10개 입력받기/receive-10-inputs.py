arr = list(map(int, input().split()))
x = []

for e in arr:
    if e == 0:
        break
    else:
        x.append(e)

s = sum(x) / len(x)

print(sum(x), end=" ")
print(f"{s:.1f}")