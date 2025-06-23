import sys

a = sys.stdin.readline()
res = 0
is_even = False

for i in range(13):
    if a[i] =="*":
        if i%2 != 0:
            is_even = True
        continue
    res += int(a[i]) * (1 if i%2==0 else 3)

if is_even:
    for i in range(10):
        if (res + i*3) %10 ==0:
            print(i)
            break
else:
    print(10 - res %10)