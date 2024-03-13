x = [0, 0, 0, 0]

for i in range(3):
    symp, temp = input().split()
    temp = int(temp)

    if symp == 'Y' and temp >= 37:
        x[0] += 1
    elif symp == 'N' and temp >= 37:
        x[1] += 1
    elif symp == 'Y' and temp < 37:
        x[2] += 1
    else:
        x[3] += 1

for e in x:
    print(e, end=" ")

if x[0] >= 2:
    print("E")