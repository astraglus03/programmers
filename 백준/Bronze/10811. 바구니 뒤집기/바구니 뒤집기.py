a,b = map(int,input().split())
c =[int(i+1) for i in range(a)]
for i in range(b):
    j,k = map(int,input().split())
    c[j-1:k] = c[j-1:k][::-1]

for i in range(a):
    print(c[i],end=' ')