n = int(input())
arr = list(map(int, input().split()))

for e in arr:
    if e % 2 == 0:
        print(e, end=" ")