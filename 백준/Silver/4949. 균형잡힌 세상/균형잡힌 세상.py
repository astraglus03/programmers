import sys

while True:
    inputs = sys.stdin.readline().rstrip()
    if inputs == '.':
        break
    stack = []
    for char in inputs:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) !=0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif char == ']':
            if len(stack) !=0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
