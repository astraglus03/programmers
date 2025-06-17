import sys
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(v):
    visited = [False] * (a + 1)
    distance = [0] * (a + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        current = queue.popleft()
        for i in lst[current]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[current]+1
                queue.append(i)
    return sum(distance)

a,b = map(int,sys.stdin.readline().split())
lst=[[] for i in range(a+1)]
cnt=sys.maxsize
ans=0

for i in range(1,b+1):
    x,y = map(int, sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)

for i in range(1,a+1):
    temp = bfs(i)
    if temp < cnt:
        cnt = temp
        ans = i
print(ans)