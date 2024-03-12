n = int(input())
sum = n
count = 0

while count < 2:
    if sum % 5 == 0:
        count += 1
    print(sum, end=" ")
    sum += n