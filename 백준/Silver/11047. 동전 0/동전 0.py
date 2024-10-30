a, b = map(int,input().split())
tmp = [int(input()) for _ in range(a)]
cnt = 0
temp = True
for i in range(len(tmp) - 1, -1, -1):
    if b // tmp[i] != 0:
        cnt += b // tmp[i]
        b %= tmp[i]

    if b == 0:
        break

print(cnt)