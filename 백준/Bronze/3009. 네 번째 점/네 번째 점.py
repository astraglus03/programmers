x=[]
y=[]
for i in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i])==1:
        j=x[i]
    if y.count(y[i])==1:
        k=y[i]
print(j,k)
