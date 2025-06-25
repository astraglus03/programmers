import sys
from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [False] * len(res)
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in res[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
            if neighbor == end:
                return True
    return False

a = int(sys.stdin.readline().strip())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
res = [[] * a for _ in range(a)]

for i in range(a):
    for j in range(a):
        if lst[i][j] == 1:
            res[i].append(j)

for i in range(a):
    for j in range(a):
        if bfs(i,j):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()