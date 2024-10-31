a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
c.pop()

cnt = 0

for i in range(len(c)):
    if i == 0 and c[i] == min(c):
        for j in b:
            cnt += c[i] * j
        break
    elif i != 0 and c[i] == min(c):
        for j in range(i, len(b)):
            cnt += c[i] * b[j]
            print(cnt)
        break
    else:
        cnt += c[i] * b[i]

print(cnt)