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
    while i <= len(b) - 1:
        if a[index] == b[i]:
            index += 1
            i += 1
        else:
            break
    is_sequnce = True

if is_sequnce:
    print("Yes")
else:
    print("No")