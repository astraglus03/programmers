import sys

a = int(sys.stdin.readline())
b = [int(sys.stdin.readline().strip()) for _ in range(a)]
b.sort()

for i in b:
    print(i)