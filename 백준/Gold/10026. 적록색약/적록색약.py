import sys
from collections import deque

def bfs(x,y,visited,grid):
    queue = deque([(x,y)])
    visited[x][y] = True
    color = grid[x][y]
    while queue:
        x,y = queue.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx, ny = x+ dx[i], y + dy[i]
            if 0<= nx < a and 0 <= ny < a and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx,ny))

a = int(sys.stdin.readline())
normal = [list(sys.stdin.readline().strip()) for _ in range(a)]
colorblind = [[c if c != "R" else "G" for c in row] for row in normal]

def count_regions(grid):
    visited = [[False] * a for i in range(a)]
    count =0
    for i in range(a):
        for j in range(a):
            if not visited[i][j]:
                bfs(i,j,visited,grid)
                count+=1
    return count

print(count_regions(normal), count_regions(colorblind))