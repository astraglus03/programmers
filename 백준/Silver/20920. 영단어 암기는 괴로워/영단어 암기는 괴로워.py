import sys
(a,b) = map(int,sys.stdin.readline().split())

tmp = {}
for i in range(a):
    c = sys.stdin.readline().rstrip()
    if c in tmp:
        tmp[c]+=1
    elif len(c)<b:
        continue
    else:
        tmp[c]=1

tmp = sorted(tmp.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in tmp:
    print(i[0])