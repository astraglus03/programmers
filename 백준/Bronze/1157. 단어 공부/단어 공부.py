a = list(str(input()).upper())
dict={}
for idx,i in enumerate(a):
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1

maxVal = max(dict.values())
keys_with_max_value = [i for i,idx in dict.items() if idx == maxVal]

if(len(keys_with_max_value)>1):
    print('?')
else:
    print(keys_with_max_value[0])
