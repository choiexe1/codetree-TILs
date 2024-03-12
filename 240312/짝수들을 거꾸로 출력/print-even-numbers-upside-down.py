n = int(input())
arr = list(map(int, input().split()))
x = []
for e in arr:
    if e % 2 == 0:
        x.append(e)

for e in x[::-1]:
    print(e, end=" ")