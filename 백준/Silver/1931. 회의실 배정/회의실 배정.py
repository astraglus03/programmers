import sys

a = int(sys.stdin.readline())
end_time = 0
cnt = 0

res=[]

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    res.append([b,c])

res.sort(key=lambda x:(x[1],x[0]))
# res.sort(key=lambda x:(x[0],x[1]))

for i in res:
    if i[0]>=end_time:
        cnt+=1
        end_time=i[1]

print(cnt)