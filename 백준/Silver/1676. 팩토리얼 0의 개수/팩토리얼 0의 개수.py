a = int(input())
tmp=1
for i in range(1,a+1):
    tmp*=i
cnt=0
while True:
    if tmp%2==0 and tmp%5==0:
        cnt+=1
        tmp//=10
    else:
        break

print(cnt)
