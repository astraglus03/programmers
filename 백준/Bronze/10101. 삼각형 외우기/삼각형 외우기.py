a = [int(input()) for i in range(3)]

if a[0] == a[1] == a[2] == 60 and sum(a)==180:
    print('Equilateral')
elif sum(a) == 180:
    if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')