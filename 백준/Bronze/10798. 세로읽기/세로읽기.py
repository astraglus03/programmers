words=''
a= [list(input()) for _ in range(5)]

max_length = max(len(b) for b in a)

for j in range(max_length):
    for i in range(5):
        if j < len(a[i]):
            words += a[i][j]
print(words)