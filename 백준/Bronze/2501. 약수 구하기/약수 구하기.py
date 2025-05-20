import sys

a,b = map(int,sys.stdin.readline().split())

tmp = []

for i in range(1,a+1):
    if(a%i==0):
        tmp.append(i)

if(len(tmp) < b):
    print('0')
else:
    print(tmp[b-1])