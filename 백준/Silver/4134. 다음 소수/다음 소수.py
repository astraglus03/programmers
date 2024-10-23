import sys
a = int(sys.stdin.readline())

def checkvalue(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(a):
    b = int(sys.stdin.readline())
    while True:
        if b==0 or b==1:
            print(2)
            break
        if checkvalue(b):
            print(b)
            break
        else:
            b+=1