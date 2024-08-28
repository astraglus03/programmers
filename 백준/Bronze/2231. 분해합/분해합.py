result = int(input())
for i in range(1,result+1):
    temp = i + sum(map(int,str(i)))
    if temp == result:
        print(i)
        break
    if i == result:
        print(0)