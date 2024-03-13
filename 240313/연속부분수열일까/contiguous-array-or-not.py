n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
l, r = 0, 0

while True:
    if count >= 2:
        break    
    
    if a[l] == b[r]:
        count += 1
    
    if r >= len(b) - 1:
        r = 0
        l += 1
    else:
        r += 1

if count > 2:
    print("Yes")
else:
    print("No")