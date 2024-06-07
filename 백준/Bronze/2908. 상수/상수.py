a =list(map(str,input().split()))

b = a[0][::-1]
c = a[1][::-1]

if(b>c):
    print(b)
else:
    print(c)