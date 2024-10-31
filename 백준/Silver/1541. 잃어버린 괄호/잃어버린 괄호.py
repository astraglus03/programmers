a = input()
res = []
tmp = ''
for i in a:
    if i=='-':
        res.append(int(tmp))
        tmp=''
        res.append(-1)
    elif i=='+':
        res.append(int(tmp))
        tmp=''
    else:
        tmp += i
res.append(int(tmp))

regard =True
res1=0
for i in res:
    if i==-1:
        regard=False
    else:
        if regard:
            res1+=i
        else:
            res1-=i

print(res1)