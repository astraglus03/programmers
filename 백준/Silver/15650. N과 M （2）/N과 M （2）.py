a, b = map(int, input().split())

res = []


def backTracking(n):
    if len(res) == b:
        print(" ".join(map(str, res)))

    for i in range(n, a + 1):
        res.append(i)
        backTracking(i + 1)
        res.pop()


backTracking(1)