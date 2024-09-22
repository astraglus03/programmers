a = int(input())
result = {}
for i in range(a):
    b, c = map(str, input().split())
    if c == 'enter':
        result[b] = True
    elif c== 'leave':
        if b in result:
            del(result[b])

result1 = sorted(result, reverse=True)
for i in result1:
    print(i)