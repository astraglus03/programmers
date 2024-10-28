a = int(input())
result = None
for i in range(0,a):
    for j in range(0,a):
        if 5*i+3*j==a:
            tmp = i+j
            if result==None:
                result = tmp
            if result>tmp:
                result = tmp

if result==None:
    print(-1)
else:
    print(result)