import sys
from collections import deque

a = int(sys.stdin.readline())

queue = deque()

for i in range(a):
    b = list(map(str, sys.stdin.readline().split()))

    if len(b)==1:
        tmp= b[0]
        if tmp=='front':
            if len(queue) !=0:
                print(queue[0])
            else:
                print(-1)

        elif tmp=='back':
            if len(queue) !=0:
                print(queue[-1])
            else:
                print(-1)
        elif tmp== 'size':
            print(len(queue))
        elif tmp=='empty':
            print(1 if len(queue) == 0 else 0)
        elif tmp=='pop':
            if len(queue) !=0:
                tmp1 = queue.popleft()
                print(tmp1)
            else:
                print(-1)
    else:
        queue.append(int(b[1]))