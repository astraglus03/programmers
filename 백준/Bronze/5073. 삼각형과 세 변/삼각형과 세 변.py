while True:
    a = list(map(int, input().split()))
    b = max(a)
    a.remove(b)
    c = min(a)
    d = max(a)
    if b==0 and c==0 and d==0:
        break
    if(b>=c+d):
        print('Invalid')
    elif b==c==d:
        print('Equilateral')
    elif b==c!=d or b!=c==d or b==d!=c:
        print('Isosceles')
    elif b!=c!=d:
        print('Scalene')