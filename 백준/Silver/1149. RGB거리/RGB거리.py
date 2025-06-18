import sys

a = int(sys.stdin.readline())
rgb = [0] * 3
tmp = [0] * 3
for i in range(a):
    m,n,k = map(int, sys.stdin.readline().split())
    if i==0:
        rgb[0] = m
        rgb[1] = n
        rgb[2] = k
        tmp[0] = m
        tmp[1] = n
        tmp[2] = k
    else:

        tmp[0] = min(rgb[1], rgb[2]) + m
        tmp[1] = min(rgb[0], rgb[2]) + n
        tmp[2] = min(rgb[0], rgb[1]) + k
        rgb[0] = tmp[0]
        rgb[1] = tmp[1]
        rgb[2] = tmp[2]
print(min(rgb))