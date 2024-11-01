a = input()
b = int(input())

for i in range(b):
    l,m,n = input().split()
    cnt=0
    for j in range(int(m),int(n)+1):
        if a[j] == l:
            cnt+=1

    print(cnt)
