a,b = map(int,input().split())
d= [0]*a
for _ in range(b):
    i, j, k = map(int, input().split())
    for f in range(i, j+1):
        d[f-1] = k

for i in range(a):
    print(d[i],end=' ')