import sys

n = int(input())
m = list(map(int, input().split()))

min = [sys.maxsize, 0]

for i in range(n):
    if m[i] < min[0]:
        min[0], min[1] = m[i], i

price = 0

for e in m[min[1]:]:
    if min[1] > e and price < min[1] - e:
        price = min[1] - e
    else:
        price = e - min[1]

print(price)