import sys

m,n = map(int,sys.stdin.readline().split())

b=dict()
c =dict()

for i in range(m):
    name=sys.stdin.readline().strip()
    b[name]=i+1
    c[i+1] = name

for j in range(n):
    tmp = sys.stdin.readline().strip()
    if tmp.isdigit():
        print(c[int(tmp)])
    else:
        print(b[tmp])