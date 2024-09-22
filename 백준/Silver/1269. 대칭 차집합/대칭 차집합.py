a,b = map(int,input().split())
e=0
f=0
c = set(int(i) for i in input().split())
d = set(int(i) for i in input().split())
for i in c:
    if i not in d:
        e+=1
for i in d:
    if i not in c:
        f+=1
print(e+f)