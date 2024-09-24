a,b = map(int,input().split())
c,d = map(int,input().split())
x,y = b,d
while b%d!=0:
    b,d = d,b%d

demo = (x*y)//d
numer = (demo//x)*a + (demo//y)*c

for i in range(max(x,y),0,-1):
    if numer%i==0 and demo%i==0:
        numer//=i
        demo//=i

print(numer, demo)