a,b =map(int,input().split())
c= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=''
while a!=0:
    result+=c[a%b]
    a //=b
print(result[::-1])