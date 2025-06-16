import sys

a,b = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

low = 1
high = max(lst)

while low<=high:
    mid = (low+high)//2

    tmp=0
    for i in lst:
        if i > mid:
            tmp+= i-mid

    if tmp>=b:
        low = mid+1
    else:
        high = mid-1

print(high)