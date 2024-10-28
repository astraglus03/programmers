import sys
from collections import deque

a = int(sys.stdin.readline())
b = deque(enumerate(map(int, sys.stdin.readline().split())))

res=[]

while b:
    idx, value = b.popleft()
    res.append(idx+1)

    if value>0:
        b.rotate(-(value-1))
    else:
        b.rotate(-value)

print(' '.join(map(str,res)))