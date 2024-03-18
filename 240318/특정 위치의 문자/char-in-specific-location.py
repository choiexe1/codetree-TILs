x = input()
n = ['L', 'E', 'B', 'R', 'O', 'S']
t = False

for i, e in enumerate(n):
    if x == e:
        t = True
        x = i


if t:
    print(x)
else:
    print("None")