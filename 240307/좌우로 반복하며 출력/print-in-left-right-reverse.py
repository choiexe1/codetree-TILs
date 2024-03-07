n = int(input())
cnt = 1

for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            if cnt <= 0:
                cnt = 1
            print(cnt, end="")
            cnt += 1
        else:
            if cnt > n:
                cnt = n
            print(cnt, end="")
            cnt -= 1
    print()