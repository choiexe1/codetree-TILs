n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def find_index(array, integer):
    for i, e in enumerate(array):
        if integer == e:
            return i
    return -1

index = find_index(a, b[0])

i = 0
is_sequnce = False

if index:
    for k in range(index, n1):
        if a[k + 1] == b[i + 1]:
            is_sequnce = True
            break
        else:
            is_sequnce = False
            break

if is_sequnce:
    print("Yes")
else:
    print("No")