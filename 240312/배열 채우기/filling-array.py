arr = list(map(int, input().split()))
x = []

for i in range(len(arr)):
    if arr[i] != 0:
        x.append(arr[i])
    else:
        break


for j in range(len(x)):
    print(x.pop(), end=" ")