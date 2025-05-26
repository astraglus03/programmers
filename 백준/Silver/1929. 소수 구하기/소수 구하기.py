import sys

a,b = map(int,sys.stdin.readline().strip().split())

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False

    return True

for i in range(a,b+1):
    if is_prime(i) and i>1:
        print(i)