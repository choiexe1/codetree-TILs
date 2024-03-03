cnt = 0
sum = 0
while True:
    age = int(input())
    if age < 30 or age > 19:
        cnt += 1
        sum += age
    else:
        print(f'{sum / cnt:.2f}')
        break