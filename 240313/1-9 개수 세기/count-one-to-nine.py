n = int(input())
arr = list(map(int, input().split()))
x = [0 for _ in range(9)]

for e in arr:
    x[e - 1] += 1

for e in x:
    print(e)