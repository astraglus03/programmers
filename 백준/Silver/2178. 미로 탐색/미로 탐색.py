# 추후 재풀이 필요

import sys
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if nx<0 or ny <0 or nx>=a or ny>=b:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

a, b = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(a)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)
print(miro[a-1][b-1])