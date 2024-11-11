import math

H,W,N,M = map(int,input().split())

count_row = math.ceil(H/(N+1))
count_col = math.ceil(W/(M+1))
print(count_col * count_row)