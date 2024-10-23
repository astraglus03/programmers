import sys
a,b = map(int,sys.stdin.readline().split())
if a<=1:
    a=2

def checkvalue(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while a<=b:
    if checkvalue(a):
        print(a)
    a+=1