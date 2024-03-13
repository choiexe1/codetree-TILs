n, q = map(int, input().split())
e = list(map(int, input().split()))

def one(index):
    print(e[index - 1])

def two(integer):
    is_exist = e.count(integer)

    if is_exist:
        print(e.index(integer) + 1)
    else:
        print(0)

def three(a, b):
    for i in range(a - 1, b):
        print(e[i], end=" ")

for _ in range(q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        one(query[1])
    elif query[0] == 2:
        two(query[1])
    else:
        three(query[1], query[2])