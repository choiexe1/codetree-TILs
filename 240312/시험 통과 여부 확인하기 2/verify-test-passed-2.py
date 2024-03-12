n = int(input())
pass_count = 0

for i in range(n):
    x = list(map(int, input().split()))
    avg = sum(x) // 4

    if avg >= 60:
        pass_count += 1
        print("pass")
    else:
        print("fail")
    
print(pass_count)