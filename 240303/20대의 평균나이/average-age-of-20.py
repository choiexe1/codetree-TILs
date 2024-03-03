cnt = 0
sum = 0
while True:
    age = int(input())
    if age > 29:
        print(f'{sum / cnt:.2f}')
        break
    else:
        cnt += 1
        sum += age