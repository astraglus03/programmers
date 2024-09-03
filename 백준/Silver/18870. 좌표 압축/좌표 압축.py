a = int(input())
b = list((map(int, input().split())))
c = sorted(set(b))
dict = {}

for i in range(0,len(c)):
    dict[c[i]] = i

for i in b:
    print(dict[i], end=' ')