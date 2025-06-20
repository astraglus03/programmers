import sys

a = int(sys.stdin.readline())
dp = []
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    dp.append(b)

for i in range(1,a):
    for j in range(0, i + 1):
        if j == 0:
            dp[i][0] = dp[i][0] + dp[i-1][0]
        elif j==i:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[a-1]))