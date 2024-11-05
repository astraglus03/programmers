c = list(map(int,input().split()))

res = sum(j**2 for j in c)

print(res%10)