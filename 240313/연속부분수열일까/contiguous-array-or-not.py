n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = a.index(b[0])
is_sequnce = True

i = 0
while i <= len(b):
    if i == len(b):
        break
    if a[x] != b[i]:
        is_sequnce = False
        break
    else:
        x += 1
        i += 1

if is_sequnce:
    print("Yes")
else:
    print("No")