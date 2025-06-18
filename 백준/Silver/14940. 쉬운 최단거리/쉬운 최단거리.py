import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((sx, sy))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if 0 <= nx < a and 0 <= ny < b and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                answer[nx][ny] = answer[x][y] + 1
                queue.append((nx, ny))

a,b = map(int,sys.stdin.readline().split())
maps=[]
answer = [[-1] * b for _ in range(a)]
visited = [[False] * b for _ in range(a)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
sx,sy =0,0

for i in range(a):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    maps.append(lst)

for i in range(a):
    for j in range(b):
        if maps[i][j] == 2:
            sx,sy = i,j

visited[sx][sy] = True
answer[sx][sy] = 0
bfs()

for i in range(a):
    for j in range(b):
        if maps[i][j] == 0:
            answer[i][j] = 0
        elif not visited[i][j]:
            answer[i][j] = -1

for i in answer:
    print(*i)