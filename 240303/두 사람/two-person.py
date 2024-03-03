a_age, a_gen = input().split()
b_age, b_gen = input().split()

if int(a_age) >= 19 or int(b_age) >= 19:
    if a_gen == "M" or b_gen == "M":
        print(1)
    else:
        print(0)
else:
    print(0)