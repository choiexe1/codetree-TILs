n = list(map(int, input().split()))

odd = sum(n[0::2])
even = sum(n[1::2])

if odd > even:
    print(odd - even)
else:
    print(even - odd)