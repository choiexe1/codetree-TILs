n = int(input())
x = list(map(int, input().split()))

max1, max2 = 0, 0

if x[0] > x[1]:
    max1, max2 = x[0], x[1]
else:
    max2, max1 = x[1], x[0]

for i in range(2, len(x)):
    if x[i] > max1:
        max1 = x[i]
    elif x[i] < max1 and x[i] > max2:
        max2 = x[i]

print(max1, max2)