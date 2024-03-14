n = int(input())
m = list(map(int, input().split()))
max = max(m)
count = [0] * (max + 1)

for e in m:
    count[e] += 1

index = -1

for i, e in enumerate(count):
    if e == 1:
        index = i

print(index)