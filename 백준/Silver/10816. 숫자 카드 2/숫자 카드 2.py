a = int(input())
b={}
for i in input().split():
    if i in b:
        b[i]+=1
    else:
        b[i]=1
c = int(input())
for i in input().split():
    if i in b:
        print(b[i],end=' ')
    else:
        print(0,end=' ')