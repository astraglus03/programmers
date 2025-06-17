import sys
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()

        for neighbor in lst[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

a,b = map(int,sys.stdin.readline().split())
lst = [[] for _ in range(a + 1)]
visited = [False] * (a + 1)


for i in range(b):
    x,y = map(int,sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)

cnt=0
for i in range(1, a + 1):
    if not visited[i]:
        bfs(i)
        cnt+=1
print(cnt)