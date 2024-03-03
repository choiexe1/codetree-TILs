n = int(input())

교실, 복도, 화장실 = 0, 0, 0

for i in range(1, n + 1):
    if i % 12 == 0:
        화장실 += 1
    elif i % 3 == 0:
        복도 += 1
    elif i % 2 == 0:
        교실 += 1

print(교실, 복도, 화장실)