a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    x,y = b,c

    while x%y!=0:
        temp = x%y
        x=y
        y=temp
    print((b * c) // y)