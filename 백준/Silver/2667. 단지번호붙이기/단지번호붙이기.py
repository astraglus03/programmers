import sys
from collections import deque

def bfs(start,end):
    queue =deque([(start,end)])
    visited[start][end] = True
    temp.append((start, end))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if 0 <= nx < a and 0 <= ny < a and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                temp.append((nx, ny))

a = int(sys.stdin.readline())
cnt=0
temp=[]
res =[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * a for _ in range(a)]
maps =[]

for i in range(a):
    b = list(*map(str, sys.stdin.readline().split()))
    tmp = []
    for j in range(len(b)):
        tmp.append(int(b[j]))
    maps.append(tmp)

for m in range(a):
    for n in range(a):
        if maps[m][n] == 1 and not visited[m][n]:
            bfs(m,n)
            cnt += 1
            res.append(len(temp))
            temp = []

res.sort()
print(cnt)
for i in res:
    print(i)