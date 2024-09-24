a = int(input())
b = sorted(([int(input()) for i in range(a)]))
small = []
for i in range(1,len(b)):
    temp = b[i] - b[i - 1]
    small.append(temp)

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def gcd_cycle(small):
    temp = small[0]
    for i in small[1:]:
        temp = gcd(temp, i)
    return temp


result = gcd_cycle(small)
result1 = 0
for i in small:
    result1+= i//result -1
print(result1)