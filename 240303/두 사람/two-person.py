a_age, a_gen = input().split()
b_age, b_gen = input().split()

if (int(a_age) >= 19 and a_gen == "M") or (int(b_age) >= 19 and b_gen == "M"):
    print(1)
else:
    print(0)