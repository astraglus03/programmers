import sys
import heapq

a = int(sys.stdin.readline())
res = []
for i in range(a):
    b = int(sys.stdin.readline())
    if b!=0:
        heapq.heappush(res,(abs(b),b))

    if b == 0:
        if len(res)>=1:
            print(heapq.heappop(res)[1])
        else:
            print(0)