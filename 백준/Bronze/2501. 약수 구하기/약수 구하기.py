a, b = map(int, input().split())
c=[]
try:
    for i in range(1, a + 1):
        if (a % i == 0):
            c.append(i)
    print(c[b-1])
except:
    print(0)