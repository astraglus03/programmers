import sys
from collections import deque

def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < c and 0 <= ny < b and 0<=nz < a and lst[nx][ny][nz] == 0:
                lst[nx][ny][nz] = lst[x][y][z] + 1
                queue.append((nx, ny, nz))

a,b,c = map(int, sys.stdin.readline().split())
lst = [[list(map(int, sys.stdin.readline().split())) for _ in range(b)] for _ in range(c)]
max_value = 0
queue = deque()

for i in range(c):
    for j in range(b):
        for k in range(a):
            if lst[i][j][k] ==1:
                queue.append((i,j,k))
bfs()

for i in range(c):
    for j in range(b):
        for k in range(a):
            if lst[i][j][k] == 0:
                print(-1)
                exit(0)
            max_value = max(max_value, lst[i][j][k])

print(max_value-1)