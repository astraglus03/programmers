import sys

a = int(sys.stdin.readline())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

tmp = factorial(a)
count=0

while(True):
    if tmp%10 != 0:
        break
    else:
        count += 1
        tmp //= 10

print(count)