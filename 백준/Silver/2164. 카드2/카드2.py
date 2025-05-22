import sys
from collections import deque

p = int(sys.stdin.readline())


def find_last(a):
    b = deque(range(1, a + 1))
    while len(b) > 1:
        b.popleft()
        b.append(b.popleft())
    return b[0]

print(find_last(p))