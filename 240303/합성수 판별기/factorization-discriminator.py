n = int(input())
s = False

for i in range(2, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        s = True

if s:
    print("C")
else:
    print("N")