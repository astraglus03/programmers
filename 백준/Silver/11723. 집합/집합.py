import sys

a = int(sys.stdin.readline())
set_list = set()

for i in range(a):
    m = list(map(str, sys.stdin.readline().split()))

    if len(m) == 1:
        if (m[0] == 'all'):
            set_list = set(list(range(1, 21)))
        else:
            set_list = set()

    else:
        n = int(m[1])
        if m[0] == 'add':
            set_list.add(n)
        elif m[0] == 'remove':
            set_list.discard(n)
        elif m[0] == 'check':
            print(1 if n in set_list else 0)
        elif m[0] == 'toggle':
            if n in set_list:
                set_list.discard(n)
            else:
                set_list.add(n)
