n = int(input())
O = True

for i in range(2, n):
    if n % i == 0:
        O = False

print('P' if O else "C")