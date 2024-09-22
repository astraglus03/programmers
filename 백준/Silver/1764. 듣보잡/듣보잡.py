a,b = map(int,input().split())
c = set()
d = set()

for _ in range(a):
    c.add(input())

for _ in range(b):
    temp = input()
    if temp in c:
        d.add(temp)

result = sorted(d)

print(len(result))
for i in result:
    print(i)