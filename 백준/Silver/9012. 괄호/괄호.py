import sys

a = int(sys.stdin.readline())

for i in range(a):
    tmp = True
    res = []
    b = sys.stdin.readline()
    for j in b:
        if j == '(':
            res.append(j)
        elif j == ')' and len(res) != 0:
            res.pop()
        elif j == ')' and len(res)==0:
            tmp = False
            break
    if tmp and len(res) ==0:
        print('YES')
    else:
        print('NO')