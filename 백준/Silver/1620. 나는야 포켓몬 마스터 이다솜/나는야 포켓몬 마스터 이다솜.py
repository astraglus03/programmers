a, b = map(int, input().split())
c = {}
e={}
for i in range(1,a+1):
    d = input()
    c[i]=d
    e[d]=i

for i in range(b):
    f = input()
    if f.isalpha() == True:
        print(e[f])
    else:
        print(c[int(f)])