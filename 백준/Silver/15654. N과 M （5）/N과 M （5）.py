import sys

def backtracking(path):
    if len(path)==b:
        print(" ".join(map(str,path)))
        return
    for i in lst:
        if i not in path:
            backtracking(path+[i])

    return;

a,b = map(int,sys.stdin.readline().split())
lst = sorted(list(map(int,sys.stdin.readline().split())))
backtracking([])
