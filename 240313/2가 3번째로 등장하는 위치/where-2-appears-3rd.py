n = int(input())
m = list(map(int, input().split()))

count = 0
index = -1

for i, e in enumerate(m):
    if count >= 3:
        break
    if e == 2:
        count += 1
        index = i + 1

print(index)