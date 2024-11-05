import sys
sys = sys.stdin.readlines

a = int(input())
b = set(list(map(int, input().split())))
c = int(input())
d = list(map(int, input().split()))

for i in d:
    if i in b:
        print(1)
    else:
        print(0)
