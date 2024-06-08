a,b =map(int, input().split())
c = [list(map(int, input().split())) for _ in range(a)]
d = [list(map(int, input().split())) for _ in range(a)]
for i in range(a):
    for j in range(b):
        print(c[i][j] + d[i][j], end=' ')
    print()