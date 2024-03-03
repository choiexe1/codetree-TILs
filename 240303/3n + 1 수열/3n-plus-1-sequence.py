n = int(input())
cnt = 0
while True:
    if n == 1:
        print(cnt)
        break
    if n % 2 != 0:
        cnt += 1
        n *= 3
        n += 1
    elif n % 2 == 0:
        cnt += 1
        n //= 2