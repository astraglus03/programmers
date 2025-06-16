import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if not visited[x][y] and board[x][y] ==1:
        visited[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

a = int(sys.stdin.readline())

for i in range(a):
    m,n,k = map(int,sys.stdin.readline().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for j in range(k):
        x,y = map(int,sys.stdin.readline().split())
        board[y][x] = 1

    for b in range(n):
        for c in range(m):
            if dfs(b,c):
                cnt+=1
    print(cnt)

