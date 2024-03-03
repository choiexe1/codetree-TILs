a, b, c = map(int, input().split())
if (c * 2) in range(a, b + 1):
    print("YES")
else:
    print("NO")