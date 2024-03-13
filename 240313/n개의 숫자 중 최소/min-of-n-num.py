n = int(input())
m = list(map(int, input().split()))

min = m[0]
count = 0

for e in m[1:]:
    if e < min:
        min = e
        count = 1
    elif e == min:
        count += 1

print(min, count)