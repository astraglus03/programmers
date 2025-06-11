import math
import sys

a = int(sys.stdin.readline())
dp=[0] *(a+1)
dp[1] = 1
for i in range(2,a+1):
    min_val = 1e9
    for j in range(1,int(math.sqrt(i))+1):
        min_val = min(min_val, dp[i-j**2])
    dp[i] = min_val+1

print(dp[a])