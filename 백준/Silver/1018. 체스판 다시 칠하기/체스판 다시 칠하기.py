import sys

m,n = map(int,sys.stdin.readline().split())

board = [sys.stdin.readline().strip() for _ in range(m)]

result=[]
for i in range(m - 7):
    for j in range(n - 7):
        cnt1 = 0  # W 체스판
        cnt2 = 0  # B 체스판
        for x in range(i,i+8):
            for y in range(j,j+8):
                current = board[x][y]
                if (x + y) % 2 == 0:
                    if current != 'W':
                        cnt1 += 1
                    if current != 'B':
                        cnt2 += 1
                else:
                    if current != 'B':
                        cnt1 += 1
                    if current != 'W':
                        cnt2 += 1
        result.append(cnt1)
        result.append(cnt2)
print(min(result))