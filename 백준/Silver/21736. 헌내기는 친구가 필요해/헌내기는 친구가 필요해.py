import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    if x<0 or x>=a or y<0 or y>=b:
        return
    if visited[x][y] or board[x][y] == 'X':
        return
    visited[x][y] = True
    if board[x][y] == 'P':
        cnt+=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)


a,b = map(int,sys.stdin.readline().split())
board = [[0] *b for j in range(a)]
visited =[[False]*b for i in range(a)]
cnt=0

for i in range(a):
    lst = [*(sys.stdin.readline().strip())]
    for j in range(len(lst)):
        board[i][j] = lst[j]

for i in range(a):
    for j in range(b):
        if board[i][j] == "I":
            dfs(i,j)

if cnt==0:
    print("TT")
else:
    print(cnt)