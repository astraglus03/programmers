import sys
arr=[]

def checkvalue(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2,123456*2):
    if checkvalue(i):
        arr.append(i)

while True:
    a = int(sys.stdin.readline())
    b = 2 * a
    if a==0:
        break
    elif a==1:
        print(1)
    else:
        tmp = [i for i in arr if a<i<=b]
        print(len(tmp))