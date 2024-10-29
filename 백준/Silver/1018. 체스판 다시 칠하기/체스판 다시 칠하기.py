a, b = map(int, input().split())
c = [input() for _ in range(a)]

white_start = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
black_start = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

res=100

for i in range(a-7):
    for j in range(b-7):
        white=0
        black=0
        for k in range(8):
            for l in range(8):
                if c[k+i][l+j] == white_start[k][l]:
                    white+=1
                if c[k+i][l+j] == black_start[k][l]:
                    black+=1
        res = min(res,white,black)

print(res)