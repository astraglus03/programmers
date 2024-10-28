import sys

n = 1000000
sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False
for i in range(2, n + 1):
    if sieve[i]:
        for j in range(i * 2, n + 1, i):
            sieve[j] = False

a = int(sys.stdin.readline())
for _ in range(a):
    b = int(sys.stdin.readline())
    count = 0
    for j in range(2, b // 2 + 1):
        if sieve[j] and sieve[b - j]:
            count += 1
    print(count)