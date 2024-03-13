n = list(map(int, input().split()))
max = 0

for e in n:
    if e > max:
        max = e

print(max)