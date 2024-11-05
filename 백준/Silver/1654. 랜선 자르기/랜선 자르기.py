import sys

sys = sys.stdin.readlines

a, b = map(int, input().split())
c = [int(input()) for _ in range(a)]

min_val = 1
max_val = max(c)

while min_val <= max_val:
    mid = (min_val + max_val) // 2
    res = sum(j // mid for j in c)

    if res>=b:
        min_val = mid + 1
    else:
        max_val = mid -1
print(max_val)
