import sys

input = sys.stdin.readline

a, b = map(int, input().split())
c = list(map(int, input().split()))

cnt = 0
res = []

for i in range(b):
    cnt += c[i]

res.append(cnt)

for i in range(b, len(c)):
    cnt += c[i] - c[i - b]
    res.append(cnt)

print(max(res))
