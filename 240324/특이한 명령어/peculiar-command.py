n = int(input())

for i in range(n):
    cmd = list(input().split())
    cmd[0], cmd[1] = int(cmd[0]), int(cmd[1])

    if cmd[2] == 's':
        print(cmd[0] * cmd[1])
    elif cmd[2] == 't':
        print((cmd[0] * cmd[1]) / 2)