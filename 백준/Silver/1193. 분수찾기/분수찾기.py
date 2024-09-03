a = int(input())
line=1
while a > line:
    a -= line
    line += 1

if line % 2 == 0:
    up = a
    down = line - a + 1
else:
    up = line - a + 1
    down = a
print(f'{up}/{down}')