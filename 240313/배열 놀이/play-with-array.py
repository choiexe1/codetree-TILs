n, q = map(int, input().split())
e = list(map(int, input().split()))

for _ in range(q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        print(e[query[1] - 1])
    elif query[0] == 2:
        idx = [0] * max(e)
        min_idx = -1

        for index, integer in enumerate(e):
            if integer == query[1]:
                if min_idx == -1:
                    min_idx = index
                idx[integer] += 1
        
        if min_idx != -1:
            print(min_idx + 1)
        else:
            print(0)
    elif query[0] == 3:
        for i in range(query[1] - 1, query[2]):
            print(e[i], end=" ")