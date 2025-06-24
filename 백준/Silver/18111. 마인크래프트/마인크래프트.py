import sys
m,n,k = map(int, sys.stdin.readline().split())
min_value =500
max_value =0
min_result = sys.maxsize
height = 0
lst=[]
for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    if min_value > min(tmp):
        min_value = min(tmp)
    if max_value < max(tmp):
        max_value = max(tmp)
    lst.append(tmp)

height_counter = [0] * 257

for i in range(m):
    for j in range(n):
        height_counter[lst[i][j]] += 1

for i in range(min_value, max_value + 1):
    total = 0
    inventory = k
    for x in range(257):
        count = height_counter[x]
        if x > i:
            diff = x - i
            total += diff * 2 * count
            inventory += diff * count
        elif x<i:
            diff = i - x
            total += diff * count
            inventory -= diff * count
    if inventory < 0:
        continue
    if total < min_result or (total == min_result and i > height):
        min_result = total
        height = i
print(min_result, height)