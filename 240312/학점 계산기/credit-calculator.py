n = float(input())
x = list(map(float, input().split()))

avg = sum(x) / n

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")

if avg >= 3.0:
    print("Good")

if avg < 3.0:
    print("Poor")