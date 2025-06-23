import sys
from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < b and 0 <= ny < a and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                queue.append((nx, ny))

a,b = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]
max_value = 0
queue = deque()

for i in range(b):
    for j in range(a):
        if lst[i][j] ==1:
            queue.append((i,j))
bfs()

for i in range(b):
    for j in range(a):
        if lst[i][j] ==0:
            print(-1)
            sys.exit()
        max_value = max(max_value, lst[i][j])

print(max_value-1)