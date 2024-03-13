n = int(input())
m = list(map(int, input().split()))

min = m[0]
count = 0

for e in m[1:]:
    if e < min:
        min = e

print(min, m.count(min))