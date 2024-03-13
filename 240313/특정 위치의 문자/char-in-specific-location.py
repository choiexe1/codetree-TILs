x = input()
n = ['L', 'E', 'B', 'R', 'O', 'S']
t = False
for index, char in enumerate(n):
    if char == x:
        print(index)
        t = True
        break

if t == False:
    print("None")