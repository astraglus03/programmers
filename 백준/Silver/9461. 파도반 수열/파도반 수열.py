import sys

p=[0,1,1,1] + [0 for _ in range(97)]
def padovan(n):
    if p[n]:
        return p[n]
    else:
        p[n] = padovan(n-2) + padovan(n-3)
        return p[n]

t = int(sys.stdin.readline())
for _ in range(t):
    a = int(sys.stdin.readline())
    print(padovan(a))