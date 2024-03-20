sum = 0
for i in range(4):
    n = list(map(int, input().split()))
    for j in range(i + 1):
        sum += n[j]

print(sum)