n = float(input())
x = list(map(float, input().split()))

avg = sum(x) / n

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")