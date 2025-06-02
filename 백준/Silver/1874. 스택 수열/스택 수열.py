import sys
from collections import deque

a = int(sys.stdin.readline())
stack = deque(int(sys.stdin.readline().strip()) for _ in range(a))
lst = []
cnt = 0
result =[]
possible = True
for i in range(1, a + 1):
    lst.append(i)
    result.append('+')
    while lst and lst[-1] == stack[cnt]:
        lst.pop()
        cnt += 1
        result.append('-')

if cnt ==a:
    for r in result:
        print(r)
else:
    print('NO')