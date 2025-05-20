import sys

inputs = sys.stdin.readline().rstrip()

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = [-1 for i in range(26)]

for i in range(len(inputs)):
    if a[alpha.index(inputs[i])] == -1:
        a[alpha.index(inputs[i])] = i

for j in a:
    print(j, end=' ')