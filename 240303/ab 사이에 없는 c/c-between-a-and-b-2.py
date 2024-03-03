a, b, c = map(int, input().split())
condition = True

for i in range(a, b + 1):
    if c / i == 0:
        condition = False

if condition:
    print("YES")
else:
    print("NO")