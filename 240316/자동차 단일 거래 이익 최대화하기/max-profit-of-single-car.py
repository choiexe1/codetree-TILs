n = int(input())
m = list(map(int, input().split()))

pp, p = 0, 1
price = 0

while pp != n - 1:
    if p == n - 1:
        p = 1
        pp += 1

    if m[pp] > m[p]:
        price = m[pp] - m[p]
        p += 1
    else:
        price = m[p] - m[pp]
        p += 1

print(price)