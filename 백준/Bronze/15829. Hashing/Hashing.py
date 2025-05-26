import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
c=[i for i in b]

sum=0
for i in range(len(c)):
   tmp = ord(c[i])-96
   sum+= tmp*31**i

print(sum)