a,b = map(int,input().split())
d = []
for i in range(a):
    d.append(i+1)

for i in range(b):
    j,k = map(int,input().split())
    temp=0
    temp = d[j-1]
    d[j-1] = d[k-1]
    d[k-1] = temp

for i in range(a):
    print(d[i],end=' ')