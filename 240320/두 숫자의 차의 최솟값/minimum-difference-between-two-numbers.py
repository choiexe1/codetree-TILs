n = int(input())
m = list(map(int, input().split()))

min = 101

for i in range(n):
    for j in range(i + 1, n):
        if m[i] > m[j]:
            if m[i] - m[j] < min:
                min = m[i] - m[j]
        else:
            if m[j] - m[i] < min:
                min = m[j] - m[i]

print(min)