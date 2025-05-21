import sys

a,b = map(int,sys.stdin.readline().split())

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

result = gcd(a,b)
print(result)
print(int(a*b/result))