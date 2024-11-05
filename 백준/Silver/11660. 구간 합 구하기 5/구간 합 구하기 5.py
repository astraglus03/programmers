import sys
input = sys.stdin.readline

a,b = map(int,input().split())

res=[list(map(int,input().split())) for _ in range(a)]
prefix_sum = [[0] * (a+1) for _ in range(a+1)]

for i in range(1,a+1):
    for j in range(1,a+1):
        prefix_sum[i][j] = res[i-1][j-1]+prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for i in range(b):
    c,d,e,f = map(int,input().split())

    print(prefix_sum[e][f] - prefix_sum[c-1][f] - prefix_sum[e][d-1] + prefix_sum[c-1][d-1])