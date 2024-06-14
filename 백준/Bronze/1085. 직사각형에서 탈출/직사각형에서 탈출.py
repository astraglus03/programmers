a = list(map(int,input().split()))
c=[]
c.append(a[0])
c.append(a[1])
c.append(a[2]-a[0])
c.append(a[3]-a[1])
print(min(c))