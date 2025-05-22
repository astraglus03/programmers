import sys

a,b = map(int,sys.stdin.readline().split())

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(a)//(factorial(b)*factorial(a-b)))