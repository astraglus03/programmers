import sys


def judge(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


a = int(sys.stdin.readline().rstrip())
if a == 0:
    print(0)
else:
    b = [int(sys.stdin.readline().rstrip()) for _ in range(a)]
    b.sort()
    remove_percent = judge(a * 0.15)

    b = b[remove_percent:a-remove_percent]
    print(judge(sum(b) / len(b)))
