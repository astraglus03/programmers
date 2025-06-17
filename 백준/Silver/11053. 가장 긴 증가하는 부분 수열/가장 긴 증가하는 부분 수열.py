import sys

a = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1] * a


for i in range(1, len(lst)):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))