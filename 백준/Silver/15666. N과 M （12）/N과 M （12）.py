# 추후 재풀이 필요

import sys

def backtracking(start):
    if len(path) == b:
        print(" ".join(map(str,path)))
        return

    for i in range(start,len(lst)):
        path.append(lst[i])
        backtracking(i)
        path.pop()

    return

a,b = map(int,sys.stdin.readline().split())
lst = sorted(set(list(map(int,sys.stdin.readline().split()))))
visited = [False] * a
path=[]
backtracking(0)
