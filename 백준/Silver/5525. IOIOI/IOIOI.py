import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = sys.stdin.readline()
i=cnt=res = 0

while i < b - 1:
    if c[i:i + 3] == "IOI":
        i += 2
        cnt += 1
        if cnt == a:
            res += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(res)
