a,b = map(int,input().split())
x,y=a,b
while x%y!=0:
    x,y = y,x%y

print((a*b)//y)