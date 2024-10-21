a = int(input())
res=[]
res.append('ChongChong')
for i in range(a):
    b,c = map(str,input().split())
    if b in res and c not in res:
        res.append(c)
    elif b not in res and c in res:
        res.append(b)

print(len(res))