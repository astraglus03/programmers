a = list(str(input().lower()))
c=[]
d = list(reversed(a))
for i in range(0,len(d)):
    c.append(d[i])
if(a==c):
    print(1)
else:
    print(0)