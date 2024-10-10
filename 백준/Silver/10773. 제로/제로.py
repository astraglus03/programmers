a = int(input())
result=[]
for i in range(a):
    b = int(input())
    if b!=0:
        result.append(b)
    else:
        result.pop()

print(sum(result))