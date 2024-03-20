arr = []

for _ in range(2):
    n = list(map(int, input().split()))
    arr.append(n)

x_sum, y_sum, total = [0, 0], [0, 0, 0, 0], 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        x_sum[i] += arr[i][j]

for index, row in enumerate(arr):
    for i, e in enumerate(row):
        y_sum[i] += row[i]
        total += row[i]

for e in x_sum:
    print(e / 4, end=" ")
print()

for e in y_sum:
    print(e / 2, end=" ")
print()

print(total / 8)