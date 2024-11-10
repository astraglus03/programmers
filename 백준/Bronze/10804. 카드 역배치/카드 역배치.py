res = [int(i) for i in range(1,21)]

for i in range(10):
    a,b = map(int,input().split())
    res[a-1:b] = res[a-1:b][::-1]

print(" ".join(map(str,res)))
