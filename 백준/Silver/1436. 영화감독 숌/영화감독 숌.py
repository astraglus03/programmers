import sys

a = int(sys.stdin.readline().strip())
num=666
count=0
while count< a:
   if '666' in str(num):
      count+=1
   num += 1

print(num-1)