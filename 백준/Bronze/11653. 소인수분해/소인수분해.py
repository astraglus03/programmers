a = int(input())
count = 2
while a>1:
    if a % count == 0:
        print(count)
        a //= count
        count = 2
    else:
        count += 1