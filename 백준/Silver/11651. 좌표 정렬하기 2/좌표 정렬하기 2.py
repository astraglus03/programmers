a = int(input())
c=[]

for i in range(0,a):
    k,j = map(int,input().split())
    c.append((k,j))

c.sort(key=lambda x:(x[1],x[0]))
for i in c:
    print(i[0], i[1])