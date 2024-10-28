import sys

a, b = map(int, sys.stdin.readline().split())
q = [int(i) for i in range(1, a + 1)]

idx = 0
res = []
while q:
    idx += b - 1
    if idx >= len(q):
        idx %= len(q)
    res.append(str(q.pop(idx)))

print('<',", ".join(res),'>',sep='')