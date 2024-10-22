a = int(input())
res = [[0] * 100 for i in range(100)]

for k in range(a):
    b, c = map(int, input().split())
    for i in range(b,b+10):
        for j in range(c,c+10):
            res[i][j]=1

result = sum([sum(i) for i in res])
print(result)