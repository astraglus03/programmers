import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    b = sys.stdin.readline().rstrip()
    stack=[]
    for char in b:
        if char =='(':
            stack.append(char)
        elif char ==')':
            if len(stack) !=0 and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(char)
                break
    print('NO' if len(stack) !=0 else 'YES')
