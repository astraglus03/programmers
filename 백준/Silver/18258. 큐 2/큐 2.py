import sys
from collections import deque

a = int(sys.stdin.readline())
res = deque([])
for i in range(a):
    b = sys.stdin.readline().split()
    if b[0] == 'push':
        res.append(int(b[1]))
    elif b[0] == 'pop':
        if len(res) == 0:
            print(-1)
        else:
            print(res.popleft())
    elif b[0] == 'size':
        print(len(res))
    elif b[0] == 'empty':
        if len(res) == 0:
            print(1)
        else:
            print(0)
    elif b[0] == 'front':
        if len(res) == 0:
            print(-1)
        else:
            print(res[0])
    elif b[0] == 'back':
        if len(res) == 0:
            print(-1)
        else:
            print(res[-1])