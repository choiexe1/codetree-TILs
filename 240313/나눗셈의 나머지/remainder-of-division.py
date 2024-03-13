a, b = map(int, input().split())
x = [0] * 9

while a >= 1:
    x[a % b] += 1
    a = a // b

r = 0

for e in x:
    if e > 0:
        r += e ** 2

print(r)