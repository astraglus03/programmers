import sys

a = int(sys.stdin.readline())

stack = []

for i in range(a):
    b = list(map(str, sys.stdin.readline().split()))

    if len(b)==1:
        tmp= b[0]
        if tmp=='top':
            if len(stack)!=0:
                print(stack[-1])
            else:
                print(-1)
        elif tmp== 'size':
            print(len(stack))
        elif tmp=='empty':
            print(1 if len(stack) == 0 else 0)
        elif tmp=='pop':
            if len(stack) !=0:
                tmp1 = stack.pop()
                print(tmp1)
            else:
                print(-1)
    else:
        stack.append(int(b[1]))