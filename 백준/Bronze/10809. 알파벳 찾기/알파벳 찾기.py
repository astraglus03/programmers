import sys

inputs = sys.stdin.readline().rstrip()

a = [-1]*26
for i in range(len(inputs)):
    idx = ord(inputs[i]) - ord('a')
    if(a[idx]== -1):
        a[idx] = i

print(*a)