a, b = map(int, input().split())

res = []


def backTracking():
    if len(res) == b:
        print(" ".join(map(str, res)))
        return

    for i in range(1, a + 1):
        res.append(i)
        backTracking()
        res.pop()


backTracking()
