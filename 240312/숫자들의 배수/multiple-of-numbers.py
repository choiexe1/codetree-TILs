n = int(input())
count = 0

while count < 2:
    if n % 5 == 0:
        count += 1
    print(n, end=" ")
    n += 4