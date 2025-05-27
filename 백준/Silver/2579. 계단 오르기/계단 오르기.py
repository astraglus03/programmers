# 추가 복습 필요

import sys

a = int(sys.stdin.readline())
stairs = [0]
dp = [0 for _ in range(a+1)]

for i in range(a):
    stairs.append(int(sys.stdin.readline().strip()))

if a==1:
    dp[1] = stairs[1]
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3,a+1):
        dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i]
print(dp[a])