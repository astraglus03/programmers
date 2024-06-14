a = int(input())
b = int(input())
c=[]
for i in range(a,b+1):
    for j in range(2,i+1):
        if(i%j==0):
            if(i==j):
                c.append(i)
            break
if(len(c)==0):
    print('-1')
else:
    print(sum(c))
    print(min(c))