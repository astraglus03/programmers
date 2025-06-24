import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())

def bfs(start,time):
    q = deque()
    q.append((start,time))
    visited = [False] * 100001
    visited[start] = True
    while q:
        x, t = q.popleft()
        if x== b:
            print(t)
            return
        nx = x - 1
        ny = x + 1
        nz = x * 2
        for i in (nx, ny, nz):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = True
                q.append((i, t + 1))

bfs(a,0)