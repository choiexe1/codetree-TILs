n = int(input())
cnt = 0

for i in range(n):
    for _ in range(n):
        cnt += 1
        print(cnt, end=" ")
    print()