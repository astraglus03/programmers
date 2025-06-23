import sys
from collections import deque

a = int(sys.stdin.readline())

for i in range(a):
    m = sys.stdin.readline().strip()
    n= int(sys.stdin.readline().strip())
    arr_input = sys.stdin.readline().strip()[1:-1]
    dq = deque(arr_input.split(",")) if arr_input else deque()

    isEmpty = False
    reverse = False

    for i in m:
        if i=="R":
            reverse = not reverse
        elif i == "D":
            if not dq:
                isEmpty = True
                break
            if reverse:
                dq.pop()
            else:
                dq.popleft()
    if isEmpty:
        print("error")
    else:
        if reverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")