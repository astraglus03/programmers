a = int(input())
result = []
result = list(set([input() for _ in range(a) if _ not in result]))
result.sort(key= lambda x:(len(x), x))
for i in result:
    print(i)