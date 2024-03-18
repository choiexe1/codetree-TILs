n = int(input())
m = list(map(int, input().split()))
x = m[0]
count = [0] * (n - 1)

for e in m[1:]:
    if e <= x:
        x = e
        count[e] += 1

print(x, count[x])