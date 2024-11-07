import sys

a = int(sys.stdin.readline())
res = set()
res1 = {i for i in range(1, 21)}
for i in range(a):
    b = sys.stdin.readline().split()

    if len(b) > 1:
        tmp = int(b[1])
    if b[0] == 'add':
        res.add(tmp)
    elif b[0] == 'check':
        if tmp in res:
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('0'+'\n')
    elif b[0] == 'remove':
        res.discard(tmp)
    elif b[0] == 'toggle':
        if tmp in res:
            res.discard(tmp)
        else:
            res.add(tmp)
    elif b[0] == 'all':
        res = {i for i in range(1,21)}
    elif b[0] == 'empty':
        res.clear()