import sys

a = int(sys.stdin.readline())
res = []


def countStack(n):
    if n == 2:
        if len(res) == 0:
            print(-1)
        else:
            print(res.pop())
    if n == 3:
        print(len(res))
    if n == 4:
        if len(res) == 0:
            print(1)
        else:
            print(0)
    if n == 5:
        if len(res) != 0:
            print(res[-1])
        else:
            print(-1)


for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    if len(b) > 1:
        res.append(b[1])
    else:
        countStack(b[0])