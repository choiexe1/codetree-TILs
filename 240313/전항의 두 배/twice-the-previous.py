arr = list(map(int, input().split()))
i = 0

while len(arr) != 12:
    x = (arr[-2] * 2) + arr[-1]
    arr.append(x)
    print(arr[i], end=" ")
    i += 1