import sys

a = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1] * a
prev = [-1] * a

for i in range(len(lst)):
    for j in range(i):
        if lst[i] > lst[j]:
            temp = dp[i]
            dp[i] = max(dp[i], dp[j]+1)
            if temp != dp[i]:
                prev[i] = j

idx=-1
max_dp = max(dp)
for i in range(a-1,-1,-1):
    if dp[i] == max_dp:
        idx = i
        break

lst2 =[]
while idx!= -1:
    lst2.append(lst[idx])
    idx = prev[idx]

lst2.reverse()
print(len(lst2))
print(*lst2)