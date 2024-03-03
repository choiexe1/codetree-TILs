n = int(input())
c = 0

for i in range(1, n):
    if i % 400 == 0 and i % 100 == 0:
        c += 1
    elif i % 100 == 0 and i % 400 != 0:
        pass
    elif i % 4 == 0:
        c += 1
print(c)