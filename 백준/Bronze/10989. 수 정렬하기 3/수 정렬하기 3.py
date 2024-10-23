import sys
a = int(sys.stdin.readline())
dict2={}
for i in range(a):
   b = int(sys.stdin.readline())
   if b in dict2.keys():
      dict2[b]+=1
   else:
      dict2[b]=1

dict1 = dict(sorted(dict2.items(),key=lambda x:(x[0],x[1])))

for k,v in dict1.items():
   for i in range(v):
      print(k)