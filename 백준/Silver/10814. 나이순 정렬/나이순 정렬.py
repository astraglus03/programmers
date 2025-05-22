import sys

a = int(sys.stdin.readline())
b=[]

for i in range(a):
    m,n = sys.stdin.readline().strip().split()
    b.append((int(m),n))

sorted_dict = sorted(b, key= lambda x:(x[0]))

for k,v in sorted_dict:
    print(k,v)