a = [list(map(int, input().split())) for _ in range(9)]
realMax = 0
real_row, real_col = 0,0

for i in range(9):
    for j in range(9):
        if(realMax<=a[i][j]):
            real_row=i+1
            real_col=j+1
            realMax = a[i][j]
print(realMax)
print(real_row,real_col)