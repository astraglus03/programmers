a,b = map(int,input().split())
sum=0
list = list(map(int,input().split()))

for i in list:
    for j in list:
        temp = 0
        temp += i
        if(i==j):
            continue
        else:
            temp+=j
        for k in list:
            if(j==k or i==k):
                continue
            else:
                temp+=k
                if(temp<=b and temp>=sum):
                    sum=temp
                    temp-=k
                else:
                    temp-=k
print(sum)