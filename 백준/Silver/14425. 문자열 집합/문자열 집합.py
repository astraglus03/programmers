a, b = map(int, input().split())
e=set()
f = 0
for i in  range(a):
    e.add(input())

for j in range(b):
    help = input()
    if help in e:
        f+=1
print(f)