n, q = map(int, input().split())
e = list(map(int, input().split()))

for _ in range(q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        print(e[query[1] - 1])
    elif query[0] == 2:
        idx = -1
        if query[1] in e:
            idx = e.index(query[1])
        print(idx + 1)
    else:
        for i in range(query[1] - 1, query[2]):
            print(e[i], end=" ")
        print()