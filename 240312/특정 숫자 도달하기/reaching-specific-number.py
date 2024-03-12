arr = list(map(int, input().split()))
sum = 0
count = 0
for i in range(len(arr)):
    if arr[i] < 250:
        count += 1
        sum += arr[i]
    
    if arr[i] >= 250:
        print(sum, end=" ")
        print(f"{sum / count:.1f}")
        break