a_age, a_gen = input().split()
b_age, b_gen = input().split()

print(1 if (int(a_age) >= 19 or int(b_age) >= 19) and (a_gen == "M" or b_gen == "M") else 0)