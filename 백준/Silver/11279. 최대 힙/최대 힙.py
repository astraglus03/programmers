import sys
import heapq

a = int(sys.stdin.readline())
max_heap = []

for i in range(a):
    b = int(sys.stdin.readline())
    if b==0:
        if len(max_heap) ==0:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap,(-b,b))