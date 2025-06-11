import sys
import heapq

a = int(sys.stdin.readline())
heap = []

for i in range(a):
    b = int(sys.stdin.readline())
    if b==0:
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,b)