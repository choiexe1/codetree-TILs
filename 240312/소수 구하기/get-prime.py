n = int(input())

for i in range(2, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")