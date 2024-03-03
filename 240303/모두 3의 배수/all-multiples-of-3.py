O = True
for _ in range(5):
    i = int(input())
    if i % 3 != 0:
        O = False

print(1 if O else 0)