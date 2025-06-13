# 추후 재풀이 필요

import sys

def backtracking():
    if len(path)==b:
        print(" ".join(map(str,path)))
        return
    for i in range(a):
        if visited[i]:
            continue
        if i>0 and lst[i] == lst[i-1] and not visited[i-1]:
            continue
        visited[i] = True
        path.append(lst[i])
        backtracking()
        path.pop()
        visited[i] = False
    return;

a,b = map(int,sys.stdin.readline().split())
lst = sorted(list(map(int,sys.stdin.readline().split())))
visited = [False] * a
path=[]
backtracking()
