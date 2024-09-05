a = int(input())
b = 1  
d = 1  

if a == 1:
    print(1)
else:
    while b < a:
        b += 6 * d  
        d += 1
    print(d)