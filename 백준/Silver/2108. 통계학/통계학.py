import sys

a = int(sys.stdin.readline())
res=[]
for i in range(a):
    res.append(int(sys.stdin.readline()))

res = sorted(res)
res3 = None
freq = {}
for i in res:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

mx = max(freq.values())
mx_dict=[]
for i in freq:
    if mx == freq[i]:
        mx_dict.append(i)
if len(mx_dict)>1:
    res3=mx_dict[1]
else:
    res3=mx_dict[0]


res1 = round(sum(res)/a)
res2 = res[len(res)//2]
res4 = max(res) - min(res)
print(f'{res1}\n{res2}\n{res3}\n{res4}')