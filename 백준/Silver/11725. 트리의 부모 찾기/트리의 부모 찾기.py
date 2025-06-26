import sys
from collections import deque

a = int(sys.stdin.readline())
lst =[[] for _ in range(a+1)]
parents = [0] * (a+1)

def bfs(start):
    queue = deque([start])
    parents[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in lst[node]:
            if parents[neighbor] == 0:
                parents[neighbor] = node
                queue.append(neighbor)

for i in range(a-1):
    x,y = map(int, sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)
bfs(1)

for i in range(2, a+1):
    print(parents[i])