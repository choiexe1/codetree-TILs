n = int(input())
x = 1

arr = [
    [0 for _ in range(n)] 
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr[j][i] = x
        x += 1

for row in arr:
    for e in row:
        print(e, end=" ")
    print()