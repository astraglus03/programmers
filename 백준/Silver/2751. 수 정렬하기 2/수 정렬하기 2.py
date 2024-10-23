import sys
a = int(sys.stdin.readline())
b = sorted([int(sys.stdin.readline()) for i in range(a)])
for i in b:
   print(i)