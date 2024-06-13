while True:
    a = int(input())
    if a == -1:
        break
    c = []
    for i in range(1, a + 1):
        if a % i == 0 and a != i:
            c.append(i)
    d = sum(c)
    if a == d:
        print(d, '=', end=' ')
        print(*c, sep=' + ')
    else:
        print(a,'is NOT perfect.')