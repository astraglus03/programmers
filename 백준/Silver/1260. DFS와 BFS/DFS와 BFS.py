import sys
from collections import deque


def dfs(g,start,visited):
    visited[start]=True
    print(start,end=' ')
    for node in sorted(g[start]):
        if not visited[node]:
            dfs(g,node,visited)

def bfs(g,start,visited1):
    queue = deque([start])
    visited1[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in sorted(g[node]):
            if not visited1[i]:
                visited1[i] = True
                queue.append(i)

m,n,k = map(int,sys.stdin.readline().split())

visited = [False]*(m+1)
visited1 = [False]*(m+1)


graph = [[] for _ in range(m+1)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(graph,k,visited)
print()
bfs(graph,k,visited1)