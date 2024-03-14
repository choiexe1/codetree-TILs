n = int(input())
x = list(map(int, input().split()))

m1, m2 = 0, 0

if x[0] > x[1]:
    m1, m2 = x[0], x[1]
else:
    m2, m1 = x[0], x[1]

for i in range(2, n):
    if x[i] >= m1:
        m2, m1 = m1, x[i]
    elif x[i] > m2:
        m2 = x[i]

print(m1, m2)