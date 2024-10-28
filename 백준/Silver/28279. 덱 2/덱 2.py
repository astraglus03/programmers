import sys
from collections import deque

a = int(sys.stdin.readline())
res = deque([])
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    if b[0] == 1:
        res.appendleft(b[1])
    elif b[0] == 2:
        res.append(b[1])
    elif b[0] == 3:
        if len(res) == 0:
            print(-1)
        else:
            print(res.popleft())
    elif b[0] == 4:
        if len(res) == 0:
            print(-1)
        else:
            print(res.pop())
    elif b[0] == 5:
        print(len(res))
    elif b[0] == 6:
        if len(res) == 0:
            print(1)
        else:
            print(0)
    elif b[0] ==7:
        if len(res) == 0:
            print(-1)
        else:
            print(res[0])
    elif b[0] == 8:
        if len(res) == 0:
            print(-1)
        else:
            print(res[-1])