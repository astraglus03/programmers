import sys
from collections import deque


def bfs1(start,end):
    q = deque()
    q.append((start,end))
    visited1[start][end] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < a and 0 <= ny < a and not visited1[nx][ny] and (lst1[nx][ny] == lst1[x][y]):
                visited1[nx][ny] = True
                q.append((nx, ny))

def bfs2(start,end):
    q = deque()
    q.append((start,end))
    visited2[start][end] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < a and 0 <= ny < a and not visited2[nx][ny] and (lst[nx][ny] == lst[x][y]):
                visited2[nx][ny] = True
                q.append((nx, ny))

a = int(sys.stdin.readline())
lst=[]
lst1=[]
visited1 = [[False] * a for _ in range(a)]
visited2 = [[False] * a for _ in range(a)]
cnt1 = 0
cnt2 = 0

for i in range(a):
    tmp = sys.stdin.readline().strip()
    tmp1=[]
    tmp2=[]
    for i in tmp:
        if i=="R":
            tmp1.append("G")
            tmp2.append(i)
        else:
            tmp1.append(i)
            tmp2.append(i)
    lst.append(tmp1)
    lst1.append(tmp2)

for i in range(a):
    for j in range(a):
        if not visited1[i][j]:
            visited1[i][j] = True
            bfs1(i,j)
            cnt1 += 1

for i in range(a):
    for j in range(a):
        if not visited2[i][j]:
            visited2[i][j] = True
            bfs2(i,j)
            cnt2 += 1

print(cnt1, cnt2)
