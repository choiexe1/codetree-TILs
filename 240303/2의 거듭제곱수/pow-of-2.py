n = int(input())
x = 0
i = 1
while True:
    if n % 2 == 0 and i * 2 == n:
        x = i
        break
    i += 1
print(x)