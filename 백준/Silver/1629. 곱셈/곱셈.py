import sys

def power(x,y):
    result = 1

    while y:
        if y%2==1:
            result *=x
        x *= x
        x = x%c
        y //= 2

    return result

a,b,c = map(int, sys.stdin.readline().split())

print(power(a,b)%c)