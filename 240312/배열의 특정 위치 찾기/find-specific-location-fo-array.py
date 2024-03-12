n = list(map(int, input().split()))
two_sum = 0
three_multiple = 0
count = 0

print(sum(n[1::2]), end=" ")
print(f"{sum(n[2::3]) / len(n[2::3]):.1f}")