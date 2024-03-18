n = list(map(int, input().split()))
max = n[0]

for e in n[1:]:
    if e > max:
        max = e

print(max)