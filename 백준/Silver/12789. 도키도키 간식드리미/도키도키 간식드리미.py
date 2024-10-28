import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
tmp = []
num = 1

for i in b:
    if i == num:
        num += 1
    else:
        tmp.append(i)

    while tmp and tmp[-1] == num:
        tmp.pop()
        num += 1

if not tmp:
    print('Nice')
else:
    print('Sad')
