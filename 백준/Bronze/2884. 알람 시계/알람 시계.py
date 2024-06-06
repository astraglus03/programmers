a,b = list(map(int,input().split()))

if(b-45<0):
    if(a<1):
        a=23
        b= 60-45+b
    else:
        a-=1
        b = 60 - 45 + b
else:
    b-=45
print(a,b)