a = list(map(int, input().split()))
b = [1,1,2,2,2,8]
c= []

for i in range(0,len(a)):
    temp = b[i]-a[i]
    c.append(temp)

for i in c:
    print(i,end=' ')