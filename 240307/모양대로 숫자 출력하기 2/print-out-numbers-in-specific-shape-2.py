n = int(input())
cnt = 2
for i in range(n):
    for _ in range(n):
        print(cnt, end=" ")
        cnt += 2
        if cnt > 8:
            cnt = 2
    print()