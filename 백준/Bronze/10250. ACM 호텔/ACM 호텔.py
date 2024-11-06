a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())


    floor = d%b #  4
    room = (d//b)+1

    if floor==0:
        floor = b
        room-=1

    print(floor*100+room)