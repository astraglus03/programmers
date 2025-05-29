# 나중에 다시 풀어보기

import sys

def custom_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


a = int(sys.stdin.readline().strip())

if a:
    stack = []
    for i in range(a):
        b = int(sys.stdin.readline().strip())
        stack.append(b)

    stack.sort()
    except_count = custom_round(a * 0.15)

    if except_count > 0:
        print(custom_round(sum(stack[except_count:-except_count]) / len(stack[except_count:-except_count])))
    else:
        print(custom_round(sum(stack) / len(stack)))
else:
   print(0)