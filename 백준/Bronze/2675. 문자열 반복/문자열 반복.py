a = int(input())

for i in range(a):
    b,c = input().split()
    for j in c:
        print(j*int(b),end='')
    print()