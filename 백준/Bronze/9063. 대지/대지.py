a = int(input())
x=[]
y=[]
for i in range(a):
    b,c = map(int,input().split())
    x.append(b)
    y.append(c)

row = max(x)-min(x)
col = max(y)-min(y)
print(row * col)
