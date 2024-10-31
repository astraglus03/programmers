a = int(input())
b = list(map(int,input().split()))

b.sort()
res=0
tmp=0

for i in range(a):
    tmp+=b[i]
    res+=tmp

print(res)