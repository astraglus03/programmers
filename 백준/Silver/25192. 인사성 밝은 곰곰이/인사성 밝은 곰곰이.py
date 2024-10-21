a = int(input())
res=set()
sum=0

for i in range(a):
    b = input()
    if b== 'ENTER':
        sum+=len(res)
        res.clear()
    else:
        res.add(b)

sum+=len(res)
print(sum)