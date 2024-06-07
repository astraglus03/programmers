import sys

a = int(sys.stdin.readline())

for i in range(a):
    b,c = list(map(int,sys.stdin.readline().split()))
    print('Case #'+str(i+1)+':',b+c)