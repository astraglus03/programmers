import sys

a = int(sys.stdin.readline().strip())

res=[]

for i in range(a//5+1):
    for j in range(a//3+1):
        tmp = a - (i*5 + j*3)
        if tmp==0:
            res.append(i+j)

if len(res)==0:
    print(-1)
else:
    print(min(res))