x = list(map(int, input().split()))
c = [0 for _ in range(6)]

for i in range(len(x)):
    if x[i] == 1: c[0] += 1
    elif x[i] == 2: c[1] += 1
    elif x[i] == 3: c[2] += 1
    elif x[i] == 4: c[3] += 1
    elif x[i] == 5: c[4] += 1
    elif x[i] == 6: c[5] += 1
    
i = 1
for e in c:
    print(f"{i} - {e}")
    i += 1