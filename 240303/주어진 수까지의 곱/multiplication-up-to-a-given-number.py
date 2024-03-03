a, b = map(int, input().split())
result = b

for i in range(a, b):
    result *= i

print(result)