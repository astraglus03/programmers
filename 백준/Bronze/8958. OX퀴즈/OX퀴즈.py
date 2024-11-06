a = int(input())

for i in range(a):
    tmp = 0
    b = list(map(str, input().split('X')))
    for i in b:
        for j in range(1,len(i)+1):
            tmp += j
    print(tmp)
