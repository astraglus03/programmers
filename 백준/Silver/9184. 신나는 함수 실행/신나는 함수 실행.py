import sys
res = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def exciting(i, j, k):
    if i <= 0 or j <= 0 or k <= 0:
        return 1
    elif i > 20 or j > 20 or k > 20:
        return exciting(20, 20, 20)
    elif res[i][j][k]:
        return res[i][j][k]
    elif i < j < k:
        res[i][j][k] = exciting(i, j, k - 1) + exciting(i, j - 1, k - 1) - exciting(i, j - 1, k)
        return res[i][j][k]

    else:
        res[i][j][k] = exciting(i - 1, j, k) + exciting(i - 1, j - 1, k) + exciting(i - 1, j, k - 1) - exciting(i - 1,j - 1,k - 1)
        return res[i][j][k]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {exciting(a,b,c)}')
