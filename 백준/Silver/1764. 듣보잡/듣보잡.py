a,b = map(int,input().split())
c = set()
d = set()

for _ in range(a):
    c.add(input())

for _ in range(b):
    d.add(input())

result = sorted(list(c & d))

print(len(result))
for i in result:
    print(i)