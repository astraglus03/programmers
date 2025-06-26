import sys
import heapq

a = int(sys.stdin.readline())

for i in range(a):
    b = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    nums = dict()

    for j in range(b):
        x, y = sys.stdin.readline().split()
        num = int(y)

        if x == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1

        elif x == "D":
            if num == 1:
                while max_heap:
                    tmp = -heapq.heappop(max_heap)
                    if nums.get(tmp, 0) > 0:
                        nums[tmp] -= 1
                        if nums[tmp] == 0:
                            del(nums[tmp])
                        break
            elif num == -1:
                while min_heap:
                    tmp1 = heapq.heappop(min_heap)
                    if nums.get(tmp1, 0) > 0:
                        nums[tmp1] -= 1
                        if nums[tmp1] == 0:
                            del(nums[tmp1])
                        break

    while max_heap and nums.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and nums.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    if not nums:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
