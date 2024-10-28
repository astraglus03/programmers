import sys
from collections import deque
res = deque([])
a = int(sys.stdin.readline())
for i in range(1,a+1):
    res.append(i)

while len(res)!=1:
    res.popleft()
    tmp = res.popleft()
    res.append(tmp)

print(res[0])