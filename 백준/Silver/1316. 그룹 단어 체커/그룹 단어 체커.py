a = int(input())
result = 0

for i in range(a):
    c = [i for i in input()]
    b = []
    tmp = True
    if len(c) == 1:
        result += 1
        continue
    for i in range(1, len(c)):
        if c[i - 1] != c[i]:
            if c[i - 1] in b:
                tmp = False
            b.append(c[i - 1])

        if c[-1] in b:
            tmp = False
    if tmp:
        result += 1
print(result)
