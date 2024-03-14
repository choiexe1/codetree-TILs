n = int(input())
m = list(map(int, input().split()))

max = m[0]
index = 0

for i, e in enumerate(m):
    if e > max:
        max = e
        index = i

print(index + 1, end=" ")
max = 0

while True:
    if index == 0:
        break
    for i in range(index):
        if m[i] > max:
            max = m[i]
            index = i
    print(index + 1, end=" ")