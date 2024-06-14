a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Equilateral')
elif a + b + c == 180 and (a == b != c or a == c != b or b == c != a):
    print('Isosceles')
elif a + b + c == 180 and a != b != c:
    print('Scalene')
elif a + b + c != 180:
    print('Error')
