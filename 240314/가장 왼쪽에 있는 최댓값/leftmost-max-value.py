n = int(input())
a = list(map(int, input().split()))

max = n

# 첫 번째 원소가 최대가 되기 전까지 계속 반복합니다.
while True:
    index = 0
    for i in range(1, max):
        if a[i] > a[index]:
            index = i

    print(index + 1, end=" ")

    if index == 0:
        break

    max = index