a=[]
for i in range(1,29):
    b = int(input())
    a.append(b)

for i in range(30):
    if(i+1 not in a):
        print(i+1)