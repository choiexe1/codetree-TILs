a, b, c = map(int, input().split())
condition = False

for i in range(a, b + 1):
    if i % c == 0:
        condition = True

print("NO" if condition else "YES")