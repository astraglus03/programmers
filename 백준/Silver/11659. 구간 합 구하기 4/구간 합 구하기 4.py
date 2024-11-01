import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = list(map(int, input().split()))

res = [0]
tmp = 0
for i in c:
    tmp += i
    res.append(tmp)

for _ in range(b):
    m, n = map(int, input().split())
    print(res[n] - res[m - 1])
