import sys

n = list(map(int, input().split()))

under, over = [], []

for e in n:
    if e > 500:
        over.append(e)
    if e < 500:
        under.append(e)

print(max(under), min(over))