a, b = map(int, input().split())

arr = [a, b]

while len(arr) != 10:
    pp, p = arr[len(arr) - 2], arr[(len(arr) - 1)]
    arr.append((p + pp) % 10)

for e in arr:
    print(e, end=" ")