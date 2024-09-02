a = int(input())
k=[]
for i in range(0,a):
    b,c = map(str,input().split())
    k.append((b,c))
k.sort(key=lambda x:int(x[0]))

for i in k:
    print(int(i[0]), i[1])